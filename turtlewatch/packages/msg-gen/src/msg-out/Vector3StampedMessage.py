from dataclasses import dataclass
from .Vector3Message import Vector3Message
from .HeaderMessage import HeaderMessage


@dataclass
class Vector3StampedMessage:
    header: HeaderMessage
    vector: Vector3Message
