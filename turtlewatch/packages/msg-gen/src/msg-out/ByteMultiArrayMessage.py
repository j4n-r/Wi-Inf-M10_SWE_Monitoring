from dataclasses import dataclass
from .byteMessage import byteMessage
from .MultiArrayLayoutMessage import MultiArrayLayoutMessage


@dataclass
class ByteMultiArrayMessage:
    layout: MultiArrayLayoutMessage
    data: list[byteMessage]
