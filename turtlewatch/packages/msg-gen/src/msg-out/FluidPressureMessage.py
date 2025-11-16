from dataclasses import dataclass
from .HeaderMessage import HeaderMessage


@dataclass
class FluidPressureMessage:
    header: HeaderMessage
    fluid_pressure: float
    variance: float
