from __future__ import annotations
import hashlib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, TypeAlias
import os

type_lookup = {
    "byte": "int",
    "bool": "bool",
    "int8": "int",
    "int16": "int",
    "int32": "int",
    "int64": "int",
    "uint8": "int",
    "uint16": "int",
    "uint32": "int",
    "uint64": "int",
    "float32": "float",
    "float64": "float",
    "string": "str",
    "char": "str",
    "bytes": "bytes",
    "time": "int",  # rospy.Time
    "duration": "int",  # rospy.Duration
}
# point = Point("home").tag("room", "Kitchen").field("temp", 21.5).field("hum", .25)

# Using point dictionary structure
points = {
    "measurement": "home",
    "tags": {"room": "Kitchen", "sensor": "K001"},
    "fields": {"temp": 72.2, "hum": 36.9, "co": 4},
    "time": 1762545600,
}


@dataclass
class Message:
    identifier: str
    imports: set[str]
    members: list[MessageField]
    __slots__: list[str] # ['header','child_frame_id','pose','twist']
    #['std_msgs/Headr','string','geometry_msgs/PoseWithCovariance','geometry_msgs/TwistWithCovariance']
    _slot_types: list[str]
    _type: str  = ""# "nav_msgs/Odometry"
    _has_header: bool  = False
@dataclass
class MessageField:
    field_type: str
    field_name: str
    is_array: bool
    default_value: Any | None = None


def main():
    files = list(Path(".").rglob("*.msg"))
    if not files:
        print("no files found")
        return
    # files = [Path("generator/msg_in/PoseWithCovariance.msg")]
    msgs = parse_from_message_file(files)
    for msg in msgs:
        write_to_file(msg)

    gen_init_file(msgs)


def parse_from_message_file(files: list[Path]) -> list[Message]:
    messages: list[Message] = []
    for file_path in files:
        msg_type = Message("", set([]), [], [],[])
        with open(file_path, "r") as file:
            lines = file.readlines()
            path = file.name
            msg_type.identifier = (
                os.path.basename(path).removesuffix(".msg") + "Message"
            )
            msg_type._type = os.path.basename(path).removesuffix(".msg")
            lines = [line.strip() for line in lines]

            for line in lines:
                if line.startswith("#") or not line:
                    continue
                words = line.split()
                is_array = False
                type = words[0]
                if "[" in type:
                    type = type.split("[")[0]
                    is_array = True
                msg_type._slot_types.append(type)
                if "/" in type:
                    type = type.split("/")[1]
                if type in type_lookup:
                    type = type_lookup[type]
                else:
                    msg_type.imports.add(type + "Message")
                    type = type + "Message"

                name = words[1]
                default_vale = None
                if "=" in name:
                    const_parts = name.split("=")
                    name = const_parts[0]
                    default_vale = const_parts[1]
                else:
                    msg_type.__slots__.append(name)

                msg_type.members.append(
                    MessageField(
                        field_type=type,
                        is_array=is_array,
                        field_name=name,
                        default_value=default_vale,
                    )
                )
        messages.append(msg_type)
    # print(messages)
    return messages


def write_to_file(msg: Message) -> None:
    imports = "".join([f"from .{imp} import {imp}\n" for imp in msg.imports])
    members: str = ""
    if not msg.members:
        members += "    pass"

    # put the fields with default values (consts) last
    sorted_members = sorted(msg.members, key=lambda x: x.default_value is not None)

    for member in sorted_members:
        if member.is_array:
            members += f"    {member.field_name}: list[{member.field_type}]\n"
        elif member.default_value:
            members += f"    {member.field_name}: {member.field_type} = {member.default_value}\n"
        else:
            members += f"    {member.field_name}: {member.field_type}\n"

    buffer = f"""from dataclasses import dataclass, field
from typing import Any
import genpy
import time
{imports}
@dataclass
class {msg.identifier}(genpy.Message):
    _type: str # topic type \\cmd_vel
{members}
    __slots__ = {msg.__slots__}
    _slot_types = {msg._slot_types}
    _has_header: bool = {msg._has_header}
    _md5sum = "{hashlib.md5(members.join(imports).encode()).hexdigest()}"
    def to_influx_point(self, tags: dict[str,str]) -> dict[str, Any]:
        return {{
            "measurement" : str(self.__class__.__name__),
            "tags": tags,
            "fields": flatten_message(self, ""),
            "time": int(time.time())
            }}

def flatten_message(msg: Any, prefix: str):
    result: dict[str, Any] = {{}}
    for k, v in msg.items():
        if isinstance(v, dict):
            new_prefix = f"{{prefix}}_{{str(k)}}" if prefix else str(k)
            result.update(flatten_message(v, new_prefix))
        else:
            key = f"{{prefix}}_{{k}}"
            result[key] = v
    return result
    """
    with open(f"./msg_gen/generator/msg_out/{msg.identifier}.py", "w") as file:
        _ = file.write(buffer)


def gen_init_file(msgs: list[Message]) -> None:
    files = list(Path("./msg_gen/generator/msg_out").rglob("*.py"))
    imports = ""
    all: list[str] = []
    for path in files:
        import_name = path.name.removesuffix(".py")
        imports += f"from .{import_name} import {import_name}\n"
        all.append(import_name)

    buffer = f"""{imports}

__all__ = ['{"','".join(all)}']
    """
    with open(f"./msg_gen/generator/msg_out/__init__.py", "w") as file:
        _ = file.write(buffer)


if __name__ == "__main__":
    main()
