from dataclasses import dataclass
from .MultiArrayLayoutMessage import MultiArrayLayoutMessage


@dataclass
class UInt16MultiArrayMessage:
    layout: MultiArrayLayoutMessage
    data: list[int]
