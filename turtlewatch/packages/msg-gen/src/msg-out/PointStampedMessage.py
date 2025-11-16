from dataclasses import dataclass
from .PointMessage import PointMessage
from .HeaderMessage import HeaderMessage


@dataclass
class PointStampedMessage:
    header: HeaderMessage
    point: PointMessage
