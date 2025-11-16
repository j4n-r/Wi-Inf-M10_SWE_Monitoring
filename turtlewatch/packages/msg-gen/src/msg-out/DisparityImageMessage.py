from dataclasses import dataclass
from .sensor_msgs/RegionOfInterestMessage import sensor_msgs/RegionOfInterestMessage
from .HeaderMessage import HeaderMessage
from .sensor_msgs/ImageMessage import sensor_msgs/ImageMessage

@dataclass
class DisparityImageMessage:
    header: HeaderMessage
    image: sensor_msgs/ImageMessage
    f: float
    T: float
    valid_window: sensor_msgs/RegionOfInterestMessage
    min_disparity: float
    max_disparity: float
    delta_d: float

    