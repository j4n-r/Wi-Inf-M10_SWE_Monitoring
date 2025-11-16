from dataclasses import dataclass


@dataclass
class MenuEntryMessage:
    id: int
    parent_id: int
    title: str
    command: str
    command_type: int
    FEEDBACK: int = 0
    ROSRUN: int = 1
    ROSLAUNCH: int = 2
