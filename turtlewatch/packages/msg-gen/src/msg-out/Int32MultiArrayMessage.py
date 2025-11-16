from dataclasses import dataclass
from .MultiArrayLayoutMessage import MultiArrayLayoutMessage


@dataclass
class Int32MultiArrayMessage:
    layout: MultiArrayLayoutMessage
    data: list[int]
