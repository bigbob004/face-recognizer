import face_recognition as fr

def get_encodings(face_img, face_location):
    return fr.face_encodings(face_img, face_location)


