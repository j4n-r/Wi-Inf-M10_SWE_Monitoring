from dataclasses import dataclass
from .WrenchMessage import WrenchMessage
from .TwistMessage import TwistMessage
from .HeaderMessage import HeaderMessage
from .TransformMessage import TransformMessage


@dataclass
class MultiDOFJointStateMessage:
    header: HeaderMessage
    joint_names: list[str]
    transforms: list[TransformMessage]
    twist: list[TwistMessage]
    wrench: list[WrenchMessage]
