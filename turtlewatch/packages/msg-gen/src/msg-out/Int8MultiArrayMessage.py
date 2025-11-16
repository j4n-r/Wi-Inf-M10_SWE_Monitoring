from dataclasses import dataclass
from .MultiArrayLayoutMessage import MultiArrayLayoutMessage


@dataclass
class Int8MultiArrayMessage:
    layout: MultiArrayLayoutMessage
    data: list[int]
