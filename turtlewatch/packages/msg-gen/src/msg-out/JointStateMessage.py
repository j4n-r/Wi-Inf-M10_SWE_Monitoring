from dataclasses import dataclass
from .HeaderMessage import HeaderMessage


@dataclass
class JointStateMessage:
    header: HeaderMessage
    name: list[str]
    position: list[float]
    velocity: list[float]
    effort: list[float]
