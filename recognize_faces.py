'''
Алгоритм распознавания:
1. Загружаем изображение
2. Выделяем лицо
3. Получаем энкодинг лица
4. Сравниваем с базой уже имеющихся лиц(энкодингов)
5. Если есть совпадение, значит мы распознали лицо, рисисуем рамку с именем человека, инача рамка с 'unknown person'
'''

from face_recognition import load_image_file, compare_faces
from detect_faces import detect_faces, set_bounding_boxes
import encode_faces


class Person_data:
    def __init__(self, person_name, person_list_encodings):
        self.person_list_encodings = person_list_encodings
        self.person_name = person_name

    def get_person_name(self, another_person_encodings):
        for known_person_encodings in self.person_list_encodings:
            if compare_faces(known_person_encodings, another_person_encodings)[0]:
                return self.person_name
        return "unknown person"

def recognize_faces(path_to_img, known_persons):
    img = load_image_file(path_to_img)
    face_locations = detect_faces(img)

    person_names = []
    for face_location in face_locations:
        person_encodings = encode_faces.get_encodings(img, [face_location])
        if len(known_persons) != 0:
            for known_person in known_persons:
                person_names.append(known_person.get_person_name(person_encodings))
        else:
            person_names.append("unknown person")



    set_bounding_boxes(face_locations, person_names, img)