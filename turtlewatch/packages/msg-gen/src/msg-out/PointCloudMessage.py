from dataclasses import dataclass
from .geometry_msgs/Point32Message import geometry_msgs/Point32Message
from .ChannelFloat32Message import ChannelFloat32Message
from .HeaderMessage import HeaderMessage

@dataclass
class PointCloudMessage:
    header: HeaderMessage
    points: list[geometry_msgs/Point32Message]
    channels: list[ChannelFloat32Message]

    