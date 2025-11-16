from dataclasses import dataclass
from .std_msgs/ColorRGBAMessage import std_msgs/ColorRGBAMessage
from .geometry_msgs/PointMessage import geometry_msgs/PointMessage
from .HeaderMessage import HeaderMessage

@dataclass
class ImageMarkerMessage:
    header: HeaderMessage
    ns: str
    id: int
    type: int
    action: int
    position: geometry_msgs/PointMessage
    scale: float
    outline_color: std_msgs/ColorRGBAMessage
    filled: int
    fill_color: std_msgs/ColorRGBAMessage
    lifetime: int
    points: list[geometry_msgs/PointMessage]
    outline_colors: list[std_msgs/ColorRGBAMessage]
    CIRCLE: int = 0
    LINE_STRIP: int = 1
    LINE_LIST: int = 2
    POLYGON: int = 3
    POINTS: int = 4
    ADD: int = 0
    REMOVE: int = 1

    