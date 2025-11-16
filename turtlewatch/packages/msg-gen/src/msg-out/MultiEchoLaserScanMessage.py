from dataclasses import dataclass
from .LaserEchoMessage import LaserEchoMessage
from .HeaderMessage import HeaderMessage


@dataclass
class MultiEchoLaserScanMessage:
    header: HeaderMessage
    angle_min: float
    angle_max: float
    angle_increment: float
    time_increment: float
    scan_time: float
    range_min: float
    range_max: float
    ranges: list[LaserEchoMessage]
    intensities: list[LaserEchoMessage]
