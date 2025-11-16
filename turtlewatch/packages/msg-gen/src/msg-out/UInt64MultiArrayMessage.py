from dataclasses import dataclass
from .MultiArrayLayoutMessage import MultiArrayLayoutMessage


@dataclass
class UInt64MultiArrayMessage:
    layout: MultiArrayLayoutMessage
    data: list[int]
