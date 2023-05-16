from abc import ABC, abstractmethod
from internal.db.db import DB


class IHandler(ABC):

    def __init__(self, _db: DB):
        self.db = _db
    @abstractmethod
    def recognize_face(self, face_img):
        pass

    @abstractmethod
    def train(self, face_img, person_name):
        pass