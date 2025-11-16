from dataclasses import dataclass
from .MultiArrayLayoutMessage import MultiArrayLayoutMessage


@dataclass
class ByteMultiArrayMessage:
    layout: MultiArrayLayoutMessage
    data: list[int]
