from dataclasses import dataclass
from .PoseMessage import PoseMessage
from .HeaderMessage import HeaderMessage


@dataclass
class PoseArrayMessage:
    header: HeaderMessage
    poses: list[PoseMessage]
