from dataclasses import dataclass
from .MultiArrayLayoutMessage import MultiArrayLayoutMessage


@dataclass
class Int64MultiArrayMessage:
    layout: MultiArrayLayoutMessage
    data: list[int]
