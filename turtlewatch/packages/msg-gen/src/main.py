from __future__ import annotations
from dataclasses import dataclass
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
    "bytes": "bytes",
    "time": "int",  # rospy.Time
    "duration": "int",  # rospy.Duration
}


@dataclass
class Message:
    identifier: str
    imports: set[str]
    members: list[MessageField]


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
    # files = [Path("src/msg-in/PoseWithCovariance.msg")]
    msgs = parse_from_message_file(files)
    for msg in msgs:
        write_to_file(msg)


def parse_from_message_file(files: list[Path]) -> list[Message]:
    messages: list[Message] = []
    for file_path in files:
        msg_type = Message("", set([]), [])
        with open(file_path, "r") as file:
            lines = file.readlines()
            path = file.name
            msg_type.identifier = (
                os.path.basename(path).removesuffix(".msg") + "Message"
            )
            lines = [line.strip() for line in lines]

            for line in lines:
                if line.startswith("#") or not line:
                    continue
                words = line.split()
                is_array = False
                type = words[0]
                if "/" in type:
                    type = type.split("/")[1]
                if "[" in type:
                    type = type.split("[")[0]
                    is_array = True
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

    buffer = f"""from dataclasses import dataclass
{imports}
@dataclass
class {msg.identifier}:
{members}
    """
    with open(f"./src/msg-out/{msg.identifier}.py", "w") as file:
        _ = file.write(buffer)


if __name__ == "__main__":
    main()
