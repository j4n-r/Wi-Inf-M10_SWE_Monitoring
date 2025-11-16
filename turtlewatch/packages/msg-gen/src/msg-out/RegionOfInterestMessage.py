from dataclasses import dataclass


@dataclass
class RegionOfInterestMessage:
    x_offset: int
    y_offset: int
    height: int
    width: int
    do_rectify: bool
