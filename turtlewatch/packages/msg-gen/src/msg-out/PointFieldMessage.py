from dataclasses import dataclass


@dataclass
class PointFieldMessage:
    INT8: int
    UINT8: int
    INT16: int
    UINT16: int
    INT32: int
    UINT32: int
    FLOAT32: int
    FLOAT64: int
    name: str
    offset: int
    datatype: int
    count: int
