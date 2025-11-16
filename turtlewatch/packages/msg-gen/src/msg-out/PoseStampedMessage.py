from dataclasses import dataclass
from .PoseMessage import PoseMessage
from .HeaderMessage import HeaderMessage


@dataclass
class PoseStampedMessage:
    header: HeaderMessage
    pose: PoseMessage
