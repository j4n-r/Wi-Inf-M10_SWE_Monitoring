from dataclasses import dataclass
from .HeaderMessage import HeaderMessage


@dataclass
class RelativeHumidityMessage:
    header: HeaderMessage
    relative_humidity: float
    variance: float
