from dataclasses import dataclass

@dataclass
class SolidPrimitiveMessage:
    BOX=1: int
    SPHERE=2: int
    CYLINDER=3: int
    CONE=4: int
    type: int
    dimensions: list[float]
    BOX_X=0: int
    BOX_Y=1: int
    BOX_Z=2: int
    SPHERE_RADIUS=0: int
    CYLINDER_HEIGHT=0: int
    CYLINDER_RADIUS=1: int
    CONE_HEIGHT=0: int
    CONE_RADIUS=1: int

    