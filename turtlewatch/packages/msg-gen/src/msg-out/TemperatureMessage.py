from dataclasses import dataclass
from .HeaderMessage import HeaderMessage


@dataclass
class TemperatureMessage:
    header: HeaderMessage
    temperature: float
    variance: float
