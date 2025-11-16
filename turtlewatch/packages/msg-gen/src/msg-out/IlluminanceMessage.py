from dataclasses import dataclass
from .HeaderMessage import HeaderMessage


@dataclass
class IlluminanceMessage:
    header: HeaderMessage
    illuminance: float
    variance: float
