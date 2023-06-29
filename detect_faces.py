from face_recognition import face_locations, load_image_file
from PIL import Image, ImageDraw, ImageFont

def detect_faces(faces_images):
    return face_locations(faces_images, model="cnn")


def set_bounding_boxes(face_location, faces_image):
    pil_img = Image.fromarray(faces_image)
    draw = ImageDraw.Draw(pil_img)

    top, right, bottom, left = face_location
    draw.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0), width=4)
    pil_img.show()
    del draw




if __name__ == "__main__":
    img_path = 'test_index/imgs/000135.jpg'
    img = load_image_file(img_path)

    location = face_locations(img, model="cnn")
    set_bounding_boxes(location[0], img)
