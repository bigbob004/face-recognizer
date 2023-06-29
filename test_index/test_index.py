import time
import os
import csv
from main import get_db_config
from internal.db.db import DB
from internal.handler.handler import Handler
from face_recognition import load_image_file
from internal.handler.handler import get_encodings_from_face
from internal import exceptions

def get_img_paths(path_to_directory):
    get_img_paths = []
    for filename in sorted(os.listdir(path_to_directory)):
        get_img_paths.append('{}/{}'.format(path_to_directory, filename))
    return get_img_paths

def get_person_ids(path_to_directory):
    person_ids = []
    with open(path_to_directory) as file:
        for line in file:
            person_ids.append(line.rstrip().split(' ')[1])
    return person_ids


def train_batch(start, size_of_batch, img_paths, person_ids, train):
    count_of_errors = 0
    print("Processing")

    i = start
    while size_of_batch != 0:
    #for i in range(start, end):
        img = load_image_file(img_paths[i])
        person_id = person_ids[i]
        is_error = False
        try:
             train(img, person_id)
        except exceptions.InvalidCountOfFaceFaceErr as error:
            count_of_errors += 1
            is_error = True
            print("something went wrong in ", i + 1, error.txt)
        except exceptions.CanNotDetectFaceErr as error:
            count_of_errors += 1
            is_error = True
            print("something went wrong in ", i + 1, error.txt)
        if is_error == False:
            size_of_batch -= 1
        print('processed {} image'.format(i + 1))
        i += 1
    print("Count of errors", count_of_errors)

    return i

def calc_search_time(writer, comparing_img_path, comparing_img_name, x_value, search_similar_face):
    comparing_image = load_image_file(comparing_img_path)
    comparing_image_embedding, _ = get_encodings_from_face(comparing_image)

    start = time.time()
    _, _, person_name = search_similar_face(comparing_image_embedding)
    end = time.time() - start
    if person_name is None or person_name != comparing_img_name:
        print("can't find face", person_name)
        return "err"

    writer.writerow([x_value, end])
    return None

if __name__ == "__main__":
    config = get_db_config('../config.yaml')
    db = DB(config)
    handler = Handler(db)

    img_paths = get_img_paths('img_align_celeba')
    person_ids = get_person_ids('identity_CelebA.txt')
    comparing_image_name = '2522'

    batch_size = 500
    count_of_imgs = 10000
    iters = count_of_imgs // batch_size


    with open('search_time_without_index.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(
            ("x_value", "search_time")
        )
        start = 0

        for i in range(1, iters + 1):
            #Заносим данные в систему
            start = train_batch(start, batch_size, img_paths, person_ids, handler.train)

            #Измеряем время
            calc_search_time(writer, 'Dev Pattale.jpg', comparing_image_name, i * batch_size, db.search_similar_face)
