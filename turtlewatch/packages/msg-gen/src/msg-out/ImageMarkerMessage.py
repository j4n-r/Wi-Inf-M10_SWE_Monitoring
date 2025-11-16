from dataclasses import dataclass
from .PointMessage import PointMessage
from .HeaderMessage import HeaderMessage
from .ColorRGBAMessage import ColorRGBAMessage


@dataclass
class ImageMarkerMessage:
    header: HeaderMessage
    ns: str
    id: int
    type: int
    action: int
    position: PointMessage
    scale: float
    outline_color: ColorRGBAMessage
    filled: int
    fill_color: ColorRGBAMessage
    lifetime: int
    points: list[PointMessage]
    outline_colors: list[ColorRGBAMessage]
    CIRCLE: int = 0
    LINE_STRIP: int = 1
    LINE_LIST: int = 2
    POLYGON: int = 3
    POINTS: int = 4
    ADD: int = 0
    REMOVE: int = 1
