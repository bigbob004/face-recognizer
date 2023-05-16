from internal.handler.interface import IHandler
from internal.exceptions import *
from face_recognition import face_encodings, face_locations


def get_encodings_from_face(face_img_arr):
    face_Locations = face_locations(face_img_arr, model="cnn")
    if len(face_Locations) == 0:
        raise CanNotDetectFaceErr
    elif len(face_Locations) > 1:
        raise InvalidCountOfFaceFaceErr
    face_embeddings = face_encodings(face_img_arr, face_Locations)
    return face_embeddings[0], face_Locations[0]


class Handler(IHandler):
    def recognize_face(self, face_img):
        face_embeddings, face_location = get_encodings_from_face(face_img)
        similar_face_entity = self.db.search_similar_face(face_embeddings)
        if similar_face_entity is None:
            raise FaceNotFoundErr
        (_, _, person_name) = similar_face_entity

        return person_name, face_location

    def train(self, face_img, person_name):
        face_embeddings, _ = get_encodings_from_face(face_img)
        similar_face_entity = self.db.search_similar_face(face_embeddings)
        if similar_face_entity is not None:
            raise AlreadyExistFaceErr
        self.db.add_new_face(face_embeddings, person_name)
