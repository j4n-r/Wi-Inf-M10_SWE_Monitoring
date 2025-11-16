from dataclasses import dataclass
from .geometry_msgs/PoseMessage import geometry_msgs/PoseMessage
from .geometry_msgs/Vector3Message import geometry_msgs/Vector3Message
from .geometry_msgs/PointMessage import geometry_msgs/PointMessage
from .std_msgs/ColorRGBAMessage import std_msgs/ColorRGBAMessage
from .HeaderMessage import HeaderMessage

@dataclass
class MarkerMessage:
    ARROW=0: int
    CUBE=1: int
    SPHERE=2: int
    CYLINDER=3: int
    LINE_STRIP=4: int
    LINE_LIST=5: int
    CUBE_LIST=6: int
    SPHERE_LIST=7: int
    POINTS=8: int
    TEXT_VIEW_FACING=9: int
    MESH_RESOURCE=10: int
    TRIANGLE_LIST=11: int
    ADD=0: int
    MODIFY=0: int
    DELETE=2: int
    DELETEALL=3: int
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

    