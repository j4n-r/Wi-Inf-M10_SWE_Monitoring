from dataclasses import dataclass


@dataclass
class LaserEchoMessage:
    echoes: list[float]
