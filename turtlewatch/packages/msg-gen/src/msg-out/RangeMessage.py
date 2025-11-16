from dataclasses import dataclass
from .HeaderMessage import HeaderMessage

@dataclass
class RangeMessage:
    header: HeaderMessage
    ULTRASOUND=0: int
    INFRARED=1: int
    radiation_type: int
    field_of_view: float
    min_range: float
    max_range: float
    range: float

    