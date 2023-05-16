from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Face(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class FaceLocation(_message.Message):
    __slots__ = ["bottom", "left", "right", "top"]
    BOTTOM_FIELD_NUMBER: _ClassVar[int]
    LEFT_FIELD_NUMBER: _ClassVar[int]
    RIGHT_FIELD_NUMBER: _ClassVar[int]
    TOP_FIELD_NUMBER: _ClassVar[int]
    bottom: int
    left: int
    right: int
    top: int
    def __init__(self, left: _Optional[int] = ..., top: _Optional[int] = ..., right: _Optional[int] = ..., bottom: _Optional[int] = ...) -> None: ...

class RecognizeFaceRequest(_message.Message):
    __slots__ = ["face"]
    FACE_FIELD_NUMBER: _ClassVar[int]
    face: Face
    def __init__(self, face: _Optional[_Union[Face, _Mapping]] = ...) -> None: ...

class RecognizeFaceResponse(_message.Message):
    __slots__ = ["face_location", "person_name"]
    FACE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    PERSON_NAME_FIELD_NUMBER: _ClassVar[int]
    face_location: FaceLocation
    person_name: str
    def __init__(self, person_name: _Optional[str] = ..., face_location: _Optional[_Union[FaceLocation, _Mapping]] = ...) -> None: ...

class TrainRequest(_message.Message):
    __slots__ = ["face", "person_name"]
    FACE_FIELD_NUMBER: _ClassVar[int]
    PERSON_NAME_FIELD_NUMBER: _ClassVar[int]
    face: Face
    person_name: str
    def __init__(self, face: _Optional[_Union[Face, _Mapping]] = ..., person_name: _Optional[str] = ...) -> None: ...
