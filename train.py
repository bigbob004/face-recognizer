'''
Псевдо-обучение
1. Загрузить фото человека
2. Получить энкодинги
3. Пройтись по базе имеющихся энкодингов, чтобы понять, есть ли такой человек в базе имеющихся (если есть, то сохранить в уже имеющиеся энкодинги),
инача сохранить новые энкодинги
4. Сохранить в формате json энкодинги и имя человека:
{
    persoName  string: encodings: int[][]
}
5. При запросе распознать лицо, подгружать данные из файлы с энкодингами

//Также можно сделать валидацию на то, что при загрузке фото для обучения, на фото не менее и не более одного лица!
//Валидация того, что на фото именно лицо (подумать, как сделать)
//Ещё валидации!!!!
//Подумай над тем, как можно ускорить очень медленный python
'''

from face_recognition import load_image_file
from encode_faces import get_encodings
from detect_faces import detect_faces
from recognize import Person_data
from os.path import splitext
import numpy as np
import json

def train(path_to_training_data, person_name, path_to_result):
    img = load_image_file(path_to_training_data)

    face_location = detect_faces(img)
    encodings = np.array(get_encodings(img, face_location))


    data = {
        person_name: encodings.tolist()
    }

    with open(path_to_result, 'w') as outfile:
        json.dump(data, outfile)

def get_persons_data(path_to_persons_data):
    with open(path_to_persons_data, 'r') as f:
        data = f.read()
        json_data = json.loads(data)

    persons_data = []
    for person_name, list_encodings in json_data.items():
        y = np.array([np.array(encodings) for encodings in list_encodings])
        persons_data.append(Person_data(person_name, y))

    return persons_data

def get_fila_name_without_extension(path_to_file):
    return splitext(path_to_file)[0]


if __name__ == "__main__":
    person_name = 'ben_2'
    train(f'training_data/{person_name}.png', person_name, 'persons_data/data.json')
