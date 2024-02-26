from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Features(_message.Message):
    __slots__ = ("id", "f1", "f2")
    ID_FIELD_NUMBER: _ClassVar[int]
    F1_FIELD_NUMBER: _ClassVar[int]
    F2_FIELD_NUMBER: _ClassVar[int]
    id: int
    f1: float
    f2: float
    def __init__(self, id: _Optional[int] = ..., f1: _Optional[float] = ..., f2: _Optional[float] = ...) -> None: ...

class Prediction(_message.Message):
    __slots__ = ("id", "prediction")
    ID_FIELD_NUMBER: _ClassVar[int]
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    id: int
    prediction: float
    def __init__(self, id: _Optional[int] = ..., prediction: _Optional[float] = ...) -> None: ...

class PredictRequest(_message.Message):
    __slots__ = ("features",)
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    features: _containers.RepeatedCompositeFieldContainer[Features]
    def __init__(self, features: _Optional[_Iterable[_Union[Features, _Mapping]]] = ...) -> None: ...

class PredictResponse(_message.Message):
    __slots__ = ("predictions",)
    PREDICTIONS_FIELD_NUMBER: _ClassVar[int]
    predictions: _containers.RepeatedCompositeFieldContainer[Prediction]
    def __init__(self, predictions: _Optional[_Iterable[_Union[Prediction, _Mapping]]] = ...) -> None: ...
