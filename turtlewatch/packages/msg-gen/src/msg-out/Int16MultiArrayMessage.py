from dataclasses import dataclass
from .MultiArrayLayoutMessage import MultiArrayLayoutMessage


@dataclass
class Int16MultiArrayMessage:
    layout: MultiArrayLayoutMessage
    data: list[int]
