from dataclasses import dataclass
from .PoseWithCovarianceMessage import PoseWithCovarianceMessage
from .HeaderMessage import HeaderMessage


@dataclass
class PoseWithCovarianceStampedMessage:
    header: HeaderMessage
    pose: PoseWithCovarianceMessage
