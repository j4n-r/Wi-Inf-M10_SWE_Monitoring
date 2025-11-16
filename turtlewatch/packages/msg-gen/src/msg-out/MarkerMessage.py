from dataclasses import dataclass
from .PoseMessage import PoseMessage
from .ColorRGBAMessage import ColorRGBAMessage
from .PointMessage import PointMessage
from .Vector3Message import Vector3Message
from .HeaderMessage import HeaderMessage


@dataclass
class MarkerMessage:
    header: HeaderMessage
    ns: str
    id: int
    type: int
    action: int
    pose: PoseMessage
    scale: Vector3Message
    color: ColorRGBAMessage
    lifetime: int
    frame_locked: bool
    points: list[PointMessage]
    colors: list[ColorRGBAMessage]
    text: str
    mesh_resource: str
    mesh_use_embedded_materials: bool
    ARROW: int = 0
    CUBE: int = 1
    SPHERE: int = 2
    CYLINDER: int = 3
    LINE_STRIP: int = 4
    LINE_LIST: int = 5
    CUBE_LIST: int = 6
    SPHERE_LIST: int = 7
    POINTS: int = 8
    TEXT_VIEW_FACING: int = 9
    MESH_RESOURCE: int = 10
    TRIANGLE_LIST: int = 11
    ADD: int = 0
    MODIFY: int = 0
    DELETE: int = 2
    DELETEALL: int = 3
