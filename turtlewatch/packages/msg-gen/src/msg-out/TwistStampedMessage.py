from dataclasses import dataclass
from .TwistMessage import TwistMessage
from .HeaderMessage import HeaderMessage


@dataclass
class TwistStampedMessage:
    header: HeaderMessage
    twist: TwistMessage
