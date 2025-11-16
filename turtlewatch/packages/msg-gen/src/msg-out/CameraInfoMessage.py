from dataclasses import dataclass
from .RegionOfInterestMessage import RegionOfInterestMessage
from .HeaderMessage import HeaderMessage


@dataclass
class CameraInfoMessage:
    header: HeaderMessage
    height: int
    width: int
    distortion_model: str
    D: list[float]
    K: list[float]
    R: list[float]
    P: list[float]
    binning_x: int
    binning_y: int
    roi: RegionOfInterestMessage
