from dataclasses import dataclass


@dataclass
class SolidPrimitiveMessage:
    type: int
    dimensions: list[float]
    BOX: int = 1
    SPHERE: int = 2
    CYLINDER: int = 3
    CONE: int = 4
    BOX_X: int = 0
    BOX_Y: int = 1
    BOX_Z: int = 2
    SPHERE_RADIUS: int = 0
    CYLINDER_HEIGHT: int = 0
    CYLINDER_RADIUS: int = 1
    CONE_HEIGHT: int = 0
    CONE_RADIUS: int = 1
