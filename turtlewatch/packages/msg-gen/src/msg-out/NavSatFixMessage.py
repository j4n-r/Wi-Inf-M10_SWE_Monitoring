from dataclasses import dataclass
from .HeaderMessage import HeaderMessage
from .NavSatStatusMessage import NavSatStatusMessage


@dataclass
class NavSatFixMessage:
    header: HeaderMessage
    status: NavSatStatusMessage
    latitude: float
    longitude: float
    altitude: float
    position_covariance: list[float]
    COVARIANCE_TYPE_UNKNOWN: int
    COVARIANCE_TYPE_APPROXIMATED: int
    COVARIANCE_TYPE_DIAGONAL_KNOWN: int
    COVARIANCE_TYPE_KNOWN: int
    position_covariance_type: int
