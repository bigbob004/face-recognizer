import os
from main import get_db_config
from internal.db.db import DB
from internal.handler.handler import Handler
from face_recognition import load_image_file
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



if __name__ == "__main__":

    config = get_db_config('../config.yaml')
    db = DB(config)
    handler = Handler(db)

    img_paths = get_img_paths('img_align_celeba')
    person_ids = get_person_ids('identity_CelebA.txt')

    count_of_errors = 0
    print("Processing")
    for i in range(1007):
        img = load_image_file(img_paths[i])
        person_id = person_ids[i]
        try:
             handler.train(img, person_id)
        except exceptions.InvalidCountOfFaceFaceErr as error:
            count_of_errors += 1
            print("something went wrong in ", i + 1, error.txt)
        except exceptions.CanNotDetectFaceErr as error:
            count_of_errors += 1
            print("something went wrong in ", i + 1, error.txt)
        print('processed {} image'.format(i + 1))
    print("Count of errors", count_of_errors)