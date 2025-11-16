from dataclasses import dataclass


@dataclass
class NavSatStatusMessage:
    STATUS_NO_FIX: int
    STATUS_FIX: int
    STATUS_SBAS_FIX: int
    STATUS_GBAS_FIX: int
    status: int
    SERVICE_GPS: int
    SERVICE_GLONASS: int
    SERVICE_COMPASS: int
    SERVICE_GALILEO: int
    service: int
