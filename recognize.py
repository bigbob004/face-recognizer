from internal.db.db import DB
from internal.handler.handler import Handler
from PIL import Image, ImageDraw
from face_recognition import load_image_file
from main import get_db_config

def set_bounding_boxes(face_location, faces_image):
    pil_img = Image.fromarray(faces_image)
    draw = ImageDraw.Draw(pil_img)

    top, right, bottom, left = face_location
    draw.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0), width=4)

    pil_img.show()


def recognize_faces(path_to_img):
    config = get_db_config('config.yaml')
    db = DB(config)
    handler = Handler(db)

    img = load_image_file(path_to_img)
    person_name, face_location = handler.recognize_face(img)
    print("got response")
    set_bounding_boxes(face_location, img)
    print(person_name)


if __name__ == "__main__":

    recognize_faces("test_index/img_align_celeba/006800.jpg")