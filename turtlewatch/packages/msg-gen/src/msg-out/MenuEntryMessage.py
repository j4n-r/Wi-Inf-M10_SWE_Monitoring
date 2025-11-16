from dataclasses import dataclass

@dataclass
class MenuEntryMessage:
    id: int
    parent_id: int
    title: str
    command: str
    FEEDBACK=0: int
    ROSRUN=1: int
    ROSLAUNCH=2: int
    command_type: int

    