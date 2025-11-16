from dataclasses import dataclass
from .Vector3Message import Vector3Message


@dataclass
class WrenchMessage:
    force: Vector3Message
    torque: Vector3Message
