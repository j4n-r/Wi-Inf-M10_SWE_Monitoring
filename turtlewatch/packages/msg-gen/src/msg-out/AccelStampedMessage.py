from dataclasses import dataclass
from .AccelMessage import AccelMessage
from .HeaderMessage import HeaderMessage


@dataclass
class AccelStampedMessage:
    header: HeaderMessage
    accel: AccelMessage
