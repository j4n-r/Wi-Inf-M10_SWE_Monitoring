from dataclasses import dataclass
from .geometry_msgs/TwistWithCovarianceMessage import geometry_msgs/TwistWithCovarianceMessage
from .HeaderMessage import HeaderMessage
from .geometry_msgs/PoseWithCovarianceMessage import geometry_msgs/PoseWithCovarianceMessage

@dataclass
class OdometryMessage:
    header: HeaderMessage
    child_frame_id: str
    pose: geometry_msgs/PoseWithCovarianceMessage
    twist: geometry_msgs/TwistWithCovarianceMessage

    