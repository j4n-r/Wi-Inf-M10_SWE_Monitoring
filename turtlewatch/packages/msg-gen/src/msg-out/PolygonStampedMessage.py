from dataclasses import dataclass
from .PolygonMessage import PolygonMessage
from .HeaderMessage import HeaderMessage


@dataclass
class PolygonStampedMessage:
    header: HeaderMessage
    polygon: PolygonMessage
