from dataclasses import dataclass
from .HeaderMessage import HeaderMessage


@dataclass
class ImageMessage:
    header: HeaderMessage
    height: int
    width: int
    encoding: str
    is_bigendian: int
    step: int
    data: list[int]
