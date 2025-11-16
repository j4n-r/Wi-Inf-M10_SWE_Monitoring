from dataclasses import dataclass
from .MultiArrayDimensionMessage import MultiArrayDimensionMessage


@dataclass
class MultiArrayLayoutMessage:
    dim: list[MultiArrayDimensionMessage]
    data_offset: int
