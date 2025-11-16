from dataclasses import dataclass
from .TwistMessage import TwistMessage


@dataclass
class TwistWithCovarianceMessage:
    twist: TwistMessage
    covariance: list[float]
