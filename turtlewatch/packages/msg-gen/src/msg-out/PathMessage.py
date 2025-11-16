from dataclasses import dataclass
from .PoseStampedMessage import PoseStampedMessage
from .HeaderMessage import HeaderMessage


@dataclass
class PathMessage:
    header: HeaderMessage
    poses: list[PoseStampedMessage]
