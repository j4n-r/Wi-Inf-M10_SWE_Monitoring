from dataclasses import dataclass
from .Vector3Message import Vector3Message


@dataclass
class AccelMessage:
    linear: Vector3Message
    angular: Vector3Message
