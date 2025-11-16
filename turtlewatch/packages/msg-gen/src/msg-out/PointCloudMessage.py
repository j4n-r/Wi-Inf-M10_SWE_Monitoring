from dataclasses import dataclass
from .Point32Message import Point32Message
from .ChannelFloat32Message import ChannelFloat32Message
from .HeaderMessage import HeaderMessage


@dataclass
class PointCloudMessage:
    header: HeaderMessage
    points: list[Point32Message]
    channels: list[ChannelFloat32Message]
