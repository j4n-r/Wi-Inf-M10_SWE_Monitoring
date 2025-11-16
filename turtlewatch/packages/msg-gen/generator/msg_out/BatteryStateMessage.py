from dataclasses import dataclass
from typing import Any
import time
from .HeaderMessage import HeaderMessage

@dataclass
class BatteryStateMessage:
    POWER_SUPPLY_STATUS_UNKNOWN: int
    POWER_SUPPLY_STATUS_CHARGING: int
    POWER_SUPPLY_STATUS_DISCHARGING: int
    POWER_SUPPLY_STATUS_NOT_CHARGING: int
    POWER_SUPPLY_STATUS_FULL: int
    POWER_SUPPLY_HEALTH_UNKNOWN: int
    POWER_SUPPLY_HEALTH_GOOD: int
    POWER_SUPPLY_HEALTH_OVERHEAT: int
    POWER_SUPPLY_HEALTH_DEAD: int
    POWER_SUPPLY_HEALTH_OVERVOLTAGE: int
    POWER_SUPPLY_HEALTH_UNSPEC_FAILURE: int
    POWER_SUPPLY_HEALTH_COLD: int
    POWER_SUPPLY_HEALTH_WATCHDOG_TIMER_EXPIRE: int
    POWER_SUPPLY_HEALTH_SAFETY_TIMER_EXPIRE: int
    POWER_SUPPLY_TECHNOLOGY_UNKNOWN: int
    POWER_SUPPLY_TECHNOLOGY_NIMH: int
    POWER_SUPPLY_TECHNOLOGY_LION: int
    POWER_SUPPLY_TECHNOLOGY_LIPO: int
    POWER_SUPPLY_TECHNOLOGY_LIFE: int
    POWER_SUPPLY_TECHNOLOGY_NICD: int
    POWER_SUPPLY_TECHNOLOGY_LIMN: int
    header: HeaderMessage
    voltage: float
    temperature: float
    current: float
    charge: float
    capacity: float
    design_capacity: float
    percentage: float
    power_supply_status: int
    power_supply_health: int
    power_supply_technology: int
    present: bool
    cell_voltage: list[float]
    cell_temperature: list[float]
    location: str
    serial_number: str

    def to_influx_point(self, tags: dict[str,str]) -> dict[str, Any]:
        return {
            "measurement" : str(self.__class__.__name__),
            "tags": tags,
            "fields": flatten_message(self, ""),
            "time": int(time.time())
            }

def flatten_message(msg: Any, prefix: str):
    result: dict[str, Any] = {}
    for k, v in msg.items():
        if isinstance(v, dict):
            new_prefix = f"{prefix}_{str(k)}" if prefix else str(k)
            result.update(flatten_message(v, new_prefix))
        else:
            key = f"{prefix}_{k}"
            result[key] = v
    return result
    