from dataclasses import dataclass
from .QuaternionMessage import QuaternionMessage
from .HeaderMessage import HeaderMessage


@dataclass
class QuaternionStampedMessage:
    header: HeaderMessage
    quaternion: QuaternionMessage
