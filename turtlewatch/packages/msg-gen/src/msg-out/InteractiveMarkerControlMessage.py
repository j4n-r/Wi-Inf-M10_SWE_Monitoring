from dataclasses import dataclass
from .MarkerMessage import MarkerMessage
from .geometry_msgs/QuaternionMessage import geometry_msgs/QuaternionMessage

@dataclass
class InteractiveMarkerControlMessage:
    name: str
    orientation: geometry_msgs/QuaternionMessage
    INHERIT: int
    FIXED: int
    VIEW_FACING: int
    orientation_mode: int
    NONE: int
    MENU: int
    BUTTON: int
    MOVE_AXIS: int
    MOVE_PLANE: int
    ROTATE_AXIS: int
    MOVE_ROTATE: int
    MOVE_3D: int
    ROTATE_3D: int
    MOVE_ROTATE_3D: int
    interaction_mode: int
    always_visible: bool
    markers: list[MarkerMessage]
    independent_marker_orientation: bool
    description: str

    