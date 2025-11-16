from dataclasses import dataclass
from .HeaderMessage import HeaderMessage


@dataclass
class LaserScanMessage:
    header: HeaderMessage
    angle_min: float
    angle_max: float
    angle_increment: float
    time_increment: float
    scan_time: float
    range_min: float
    range_max: float
    ranges: list[float]
    intensities: list[float]
