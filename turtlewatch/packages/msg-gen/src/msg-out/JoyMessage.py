from dataclasses import dataclass
from .HeaderMessage import HeaderMessage


@dataclass
class JoyMessage:
    header: HeaderMessage
    axes: list[float]
    buttons: list[int]
