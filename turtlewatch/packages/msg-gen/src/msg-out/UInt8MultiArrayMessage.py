from dataclasses import dataclass
from .MultiArrayLayoutMessage import MultiArrayLayoutMessage


@dataclass
class UInt8MultiArrayMessage:
    layout: MultiArrayLayoutMessage
    data: list[int]
