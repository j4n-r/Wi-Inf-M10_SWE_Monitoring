from dataclasses import dataclass
from .HeaderMessage import HeaderMessage


@dataclass
class CompressedImageMessage:
    header: HeaderMessage
    format: str
    data: list[int]
