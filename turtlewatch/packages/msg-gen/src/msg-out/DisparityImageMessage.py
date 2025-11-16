from dataclasses import dataclass
from .RegionOfInterestMessage import RegionOfInterestMessage
from .ImageMessage import ImageMessage
from .HeaderMessage import HeaderMessage


@dataclass
class DisparityImageMessage:
    header: HeaderMessage
    image: ImageMessage
    f: float
    T: float
    valid_window: RegionOfInterestMessage
    min_disparity: float
    max_disparity: float
    delta_d: float
