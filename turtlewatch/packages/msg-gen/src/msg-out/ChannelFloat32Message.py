from dataclasses import dataclass


@dataclass
class ChannelFloat32Message:
    name: str
    values: list[float]
