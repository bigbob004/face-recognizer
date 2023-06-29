import psycopg2
from pgvector.psycopg2 import register_vector
from copy import copy

VALID_DISTANCE = 0.5
#TODO константы для названия табличек

#TODO подумать: ретраи при обрывае соединения с базой


class DB:
    def __init__(self, config):
        _conn = None
        database_config = config
        try:
            # пытаемся подключиться к базе данных
            _conn = psycopg2.connect(**database_config)
            _conn.autocommit = True
            register_vector(_conn)

            self.conn = _conn
            print('Connection is succesful')
        except(Exception, psycopg2.DatabaseError) as error:
            # в случае сбоя подключения будет выведено сообщение  в STDOUT
            print('Can`t establish connection to database: ', error)
            raise

    def add_new_face(self, face_encodings, person_name):
        query = None
        try:
            with self.conn.cursor() as curs:
                curs.execute('INSERT INTO faces_embeddings (embeddings, person_name) VALUES (%s, %s)', (face_encodings, person_name))
                query = copy(curs.query)
        except(Exception, psycopg2.DatabaseError) as error:
            print(f'Can not execute query: {query}, error: {error}')
            raise


    def search_similar_face(self, face_encodings):
        query = None
        try:
            with self.conn.cursor() as curs:
                curs.execute('SELECT * FROM faces_embeddings WHERE embeddings <-> %s < %s', (face_encodings, VALID_DISTANCE))
                similar_face = curs.fetchone()
                query = copy(curs.query)
                return similar_face
        except(Exception, psycopg2.DatabaseError) as error:
            print(f'Can not execute query: {query}, error: {error}')
            raise
