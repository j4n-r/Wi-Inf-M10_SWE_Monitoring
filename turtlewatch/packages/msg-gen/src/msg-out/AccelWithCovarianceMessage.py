from dataclasses import dataclass
from .AccelMessage import AccelMessage


@dataclass
class AccelWithCovarianceMessage:
    accel: AccelMessage
    covariance: list[float]
