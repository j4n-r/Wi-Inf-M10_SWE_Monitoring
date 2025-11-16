from dataclasses import dataclass
from .MultiArrayLayoutMessage import MultiArrayLayoutMessage


@dataclass
class Float64MultiArrayMessage:
    layout: MultiArrayLayoutMessage
    data: list[float]
