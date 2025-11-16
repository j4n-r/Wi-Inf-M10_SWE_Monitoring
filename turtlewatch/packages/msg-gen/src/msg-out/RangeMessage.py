from dataclasses import dataclass
from .HeaderMessage import HeaderMessage


@dataclass
class RangeMessage:
    header: HeaderMessage
    radiation_type: int
    field_of_view: float
    min_range: float
    max_range: float
    range: float
    ULTRASOUND: int = 0
    INFRARED: int = 1
