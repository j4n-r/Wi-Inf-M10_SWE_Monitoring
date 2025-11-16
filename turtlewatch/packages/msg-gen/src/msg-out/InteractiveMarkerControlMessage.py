from dataclasses import dataclass
from .QuaternionMessage import QuaternionMessage
from .MarkerMessage import MarkerMessage


@dataclass
class InteractiveMarkerControlMessage:
    name: str
    orientation: QuaternionMessage
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
