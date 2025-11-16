from dataclasses import dataclass


@dataclass
class MultiArrayDimensionMessage:
    label: str
    size: int
    stride: int
