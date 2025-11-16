from dataclasses import dataclass
from .MultiArrayLayoutMessage import MultiArrayLayoutMessage


@dataclass
class Float32MultiArrayMessage:
    layout: MultiArrayLayoutMessage
    data: list[float]
