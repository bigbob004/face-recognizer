import grpc

import face_recognizer_api_pb2_grpc
import face_recognizer_api_pb2
from google.protobuf import empty_pb2
from internal.handler.interface import IHandler
from internal.api.mapping.map_from_bytes_to_nparray import convert_bytes_to_nparray
from internal.exceptions import *

#TODO прикрутить типизацию
class FaceRecognizerServicer(face_recognizer_api_pb2_grpc.FaceRecognizerServicer):

    def __init__(self, _handler: IHandler):
        self.handler = _handler

    def RecognizeFace(self, request, context):

        if len(request.face.data) == 0:
            #TODO сюда прописать пояснения
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return face_recognizer_api_pb2.RecognizeFaceResponse()
        try:
            #b = None
            #with open("/Users/venemakrb/PycharmProjects/face_recognizer/bred_pit.png", "rb") as image:
                #b = image.read()
            #converted_face = convert_bytes_to_nparray(b)
            converted_face = convert_bytes_to_nparray(request.face.data)
            _person_name, face_location = self.handler.recognize_face(converted_face)
        except (CanNotDetectFaceErr, InvalidCountOfFaceFaceErr, FaceNotFoundErr) as exception:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(exception.txt)
            return face_recognizer_api_pb2.RecognizeFaceResponse()
        except BaseException as exception:
            context.set_code(grpc.StatusCode.INTERNAL)
            print(exception)
            return face_recognizer_api_pb2.RecognizeFaceResponse()
        else:
            _top, _right, _bottom, _left = face_location
            response = face_recognizer_api_pb2.RecognizeFaceResponse(person_name=_person_name, face_location=face_recognizer_api_pb2.FaceLocation(left=_left, top=_top, right=_right, bottom=_bottom))
            context.set_code(grpc.StatusCode.OK)
            return response

    def Train(self, request, context):
        if len(request.face.data) == 0 or len(request.person_name) == 0:
            # TODO сюда прописать пояснения
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return face_recognizer_api_pb2.RecognizeFaceResponse()

        try:
            #b = None
            #with open("/Users/venemakrb/PycharmProjects/face_recognizer/bred_pit.png", "rb") as image:
                #b = image.read()
            #converted_face = convert_bytes_to_nparray(b)
            converted_face = convert_bytes_to_nparray(request.face.data)
            person_name = request.person_name
            self.handler.train(converted_face, person_name)
        except (CanNotDetectFaceErr, AlreadyExistFaceErr, InvalidCountOfFaceFaceErr) as exception:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(exception.txt)
        except BaseException as exception:
            context.set_code(grpc.StatusCode.INTERNAL)
        else:
            context.set_code(grpc.StatusCode.OK)
        finally:
            return empty_pb2.Empty()


