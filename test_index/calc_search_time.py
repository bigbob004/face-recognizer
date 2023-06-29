import time
import os
import csv
from main import get_db_config
from internal.db.db import DB
from face_recognition import load_image_file
from internal.handler.handler import get_encodings_from_face
from internal import exceptions


def get_img_paths(path_to_directory):
    get_img_paths = []
    for filename in os.listdir(path_to_directory):
        get_img_paths.append('{}/{}'.format(path_to_directory, filename))
    return get_img_paths

def get_person_ids(path_to_directory):
    person_ids = []
    with open(path_to_directory) as file:
        for line in file:
            person_ids.append(line.rstrip().split(' ')[1])
    return person_ids

if __name__ == "__main__":

    config = get_db_config('../config.yaml')
    db = DB(config)

    comparing_image_name = '2522'
    comparing_image = load_image_file('Dev Pattale.jpg')
    comparing_image_embedding, _ = get_encodings_from_face(comparing_image)

    search_times = []

    with open('search_time_without_index.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(
            ("x_value", "search_time")
        )

    for i in range(500, 1001, 500):
        start = time.time()
        _, _, person_name = db.search_similar_face_for_test(comparing_image_embedding, i)
        end = time.time() - start
        if person_name is None or person_name != comparing_image_name:
            print("can't find face", person_name)
            break
        search_times.append([i, end])

    for search_time in search_times:
        with open('search_time_without_index.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(search_time)
