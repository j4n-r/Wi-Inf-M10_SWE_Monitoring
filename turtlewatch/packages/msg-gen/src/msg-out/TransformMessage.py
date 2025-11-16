from dataclasses import dataclass
from .Vector3Message import Vector3Message
from .QuaternionMessage import QuaternionMessage


@dataclass
class TransformMessage:
    translation: Vector3Message
    rotation: QuaternionMessage
