from dataclasses import dataclass
from .HeaderMessage import HeaderMessage


@dataclass
class TimeReferenceMessage:
    header: HeaderMessage
    time_ref: int
    source: str
