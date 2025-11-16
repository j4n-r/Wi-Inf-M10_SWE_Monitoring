from dataclasses import dataclass
from .WrenchMessage import WrenchMessage
from .HeaderMessage import HeaderMessage


@dataclass
class WrenchStampedMessage:
    header: HeaderMessage
    wrench: WrenchMessage
