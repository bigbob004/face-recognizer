from face_recognition import face_locations
from PIL import Image, ImageDraw, ImageFont

def detect_faces(faces_images):
    return face_locations(faces_images, model="cnn")


def set_bounding_boxes(face_locations, person_names, faces_image):
    pil_img = Image.fromarray(faces_image)
    draw = ImageDraw.Draw(pil_img)

    for(i, location) in enumerate(face_locations):
        top, right, bottom, left = location
        draw.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0), width=4)
        size = int(0.07 * (right - left))
        draw.text((left, bottom), person_names[i], font=ImageFont.truetype(font="arial.ttf", size=30))

    del draw
    pil_img.save("result/result.jpg")