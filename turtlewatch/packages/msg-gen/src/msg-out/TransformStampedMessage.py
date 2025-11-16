from dataclasses import dataclass
from .HeaderMessage import HeaderMessage
from .TransformMessage import TransformMessage


@dataclass
class TransformStampedMessage:
    header: HeaderMessage
    child_frame_id: str
    transform: TransformMessage
