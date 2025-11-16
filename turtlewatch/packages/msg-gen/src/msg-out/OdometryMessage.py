from dataclasses import dataclass
from .PoseWithCovarianceMessage import PoseWithCovarianceMessage
from .TwistWithCovarianceMessage import TwistWithCovarianceMessage
from .HeaderMessage import HeaderMessage


@dataclass
class OdometryMessage:
    header: HeaderMessage
    child_frame_id: str
    pose: PoseWithCovarianceMessage
    twist: TwistWithCovarianceMessage
