from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PetRequests(_message.Message):
    __slots__ = ("name", "gender", "age", "breed")
    NAME_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    BREED_FIELD_NUMBER: _ClassVar[int]
    name: str
    gender: str
    age: str
    breed: str
    def __init__(self, name: _Optional[str] = ..., gender: _Optional[str] = ..., age: _Optional[str] = ..., breed: _Optional[str] = ...) -> None: ...

class PetListResponse(_message.Message):
    __slots__ = ("pets",)
    PETS_FIELD_NUMBER: _ClassVar[int]
    pets: _containers.RepeatedCompositeFieldContainer[PetRequests]
    def __init__(self, pets: _Optional[_Iterable[_Union[PetRequests, _Mapping]]] = ...) -> None: ...

class SearchRequest(_message.Message):
    __slots__ = ("type", "query")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    type: str
    query: str
    def __init__(self, type: _Optional[str] = ..., query: _Optional[str] = ...) -> None: ...

class RegisterResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...
