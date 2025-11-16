from dataclasses import dataclass


@dataclass
class KeyValueMessage:
    key: str
    value: str
