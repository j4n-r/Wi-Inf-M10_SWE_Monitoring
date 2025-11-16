from dataclasses import dataclass
from .geometry_msgs/PoseMessage import geometry_msgs/PoseMessage
from .geometry_msgs/Vector3Message import geometry_msgs/Vector3Message
from .geometry_msgs/PointMessage import geometry_msgs/PointMessage
from .std_msgs/ColorRGBAMessage import std_msgs/ColorRGBAMessage
from .HeaderMessage import HeaderMessage

@dataclass
class MarkerMessage:
    header: HeaderMessage
    ns: str
    id: int
    type: int
    action: int
    pose: geometry_msgs/PoseMessage
    scale: geometry_msgs/Vector3Message
    color: std_msgs/ColorRGBAMessage
    lifetime: int
    frame_locked: bool
    points: list[geometry_msgs/PointMessage]
    colors: list[std_msgs/ColorRGBAMessage]
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

    