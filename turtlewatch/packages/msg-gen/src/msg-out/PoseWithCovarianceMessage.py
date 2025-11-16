from dataclasses import dataclass
from .PoseMessage import PoseMessage


@dataclass
class PoseWithCovarianceMessage:
    pose: PoseMessage
    covariance: list[float]
