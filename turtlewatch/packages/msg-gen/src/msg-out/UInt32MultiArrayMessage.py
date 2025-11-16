from dataclasses import dataclass
from .MultiArrayLayoutMessage import MultiArrayLayoutMessage


@dataclass
class UInt32MultiArrayMessage:
    layout: MultiArrayLayoutMessage
    data: list[int]
