from concurrent import futures

import grpc

import face_recognizer_api_pb2_grpc
from internal.handler.handler import Handler
from internal.db.db import DB
import yaml
from internal.api.face_recognizer_servicer import FaceRecognizerServicer

def get_db_config(config_file_name="config.yaml"):
    with open(config_file_name, 'r') as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def serve():
    try:
        config = get_db_config()
        db = DB(config)
        handler = Handler(db)

        server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
        face_recognizer_api_pb2_grpc.add_FaceRecognizerServicer_to_server(FaceRecognizerServicer(handler), server)

        # запускаемся на порту 6066
        print('Starting server on port 6066.')
        server.add_insecure_port('[::]:6066')
        server.start()
        server.wait_for_termination()
    except BaseException as error:
        print("Can't start server, err is", error)

#TODO прикрутить индекс в БД
#TODO валидация размера файла с изображением
if __name__ == "__main__":
    serve()