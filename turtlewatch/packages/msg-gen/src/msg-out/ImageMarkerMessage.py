from dataclasses import dataclass
from .std_msgs/ColorRGBAMessage import std_msgs/ColorRGBAMessage
from .geometry_msgs/PointMessage import geometry_msgs/PointMessage
from .HeaderMessage import HeaderMessage

@dataclass
class ImageMarkerMessage:
    CIRCLE=0: int
    LINE_STRIP=1: int
    LINE_LIST=2: int
    POLYGON=3: int
    POINTS=4: int
    ADD=0: int
    REMOVE=1: int
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

    