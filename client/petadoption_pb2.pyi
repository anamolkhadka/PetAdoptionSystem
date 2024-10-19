from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PetInfo(_message.Message):
    __slots__ = ("name", "gender", "age", "breed", "picture")
    NAME_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    BREED_FIELD_NUMBER: _ClassVar[int]
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    name: str
    gender: str
    age: int
    breed: str
    picture: bytes
    def __init__(self, name: _Optional[str] = ..., gender: _Optional[str] = ..., age: _Optional[int] = ..., breed: _Optional[str] = ..., picture: _Optional[bytes] = ...) -> None: ...

class RegistrationResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...

class SearchRequest(_message.Message):
    __slots__ = ("query",)
    QUERY_FIELD_NUMBER: _ClassVar[int]
    query: str
    def __init__(self, query: _Optional[str] = ...) -> None: ...

class PetList(_message.Message):
    __slots__ = ("pets",)
    PETS_FIELD_NUMBER: _ClassVar[int]
    pets: _containers.RepeatedCompositeFieldContainer[PetInfo]
    def __init__(self, pets: _Optional[_Iterable[_Union[PetInfo, _Mapping]]] = ...) -> None: ...
