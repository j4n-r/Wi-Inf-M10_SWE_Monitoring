from dataclasses import dataclass
from .MarkerMessage import MarkerMessage


@dataclass
class MarkerArrayMessage:
    markers: list[MarkerMessage]
