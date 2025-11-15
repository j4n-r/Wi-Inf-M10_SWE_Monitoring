from __future__ import annotations
from dataclasses import dataclass
from typing import TypeAlias
import os

type_lookup = {"float64": "int"}
FieldType: TypeAlias = str
FieldName: TypeAlias = str


# type = [(int, x), (int, y)]


@dataclass
class MessageType:
    identifier: str
    imports: set[str]
    members: list[tuple[FieldType, FieldName]]

def main():
    msgs = parse_from_message_file(["./src/Vector3.msg", "./src/Twist.msg"])
    for msg in msgs:
        write_to_file(msg)

def parse_from_message_file(files: list[str]) -> list[MessageType]:
    messages: list[MessageType] = []
    for file_path in files:
        msg_type = MessageType("",set([]), [])
        with open(file_path, "r") as file:
            lines = file.readlines()
            path = file.name
            msg_type.identifier = os.path.basename(path).removesuffix(".msg") + "Message"
            lines = [line.strip() for line in lines]

            for line in lines:
                if line.startswith("#") or not line:
                    continue
                words = line.split()
                type = words[0]
                if type in type_lookup:
                    type = type_lookup[type]
                else:
                    msg_type.imports.add(type+"Message")
                    type = type+"Message"
                name = words[1]
                msg_type.members.append((type, name))
        messages.append(msg_type)

    return messages


def write_to_file(msg: MessageType) -> None:

    imports = "".join([f"from .{imp} import {imp}\n" for imp in msg.imports])
    members = "".join([
        f"    {field_type}: {field_name}\n" for field_name, field_type in msg.members
    ])
    buffer = f"""from dataclasses import dataclass
{imports}
@dataclass
class {msg.identifier}:
{members}
    """
    with open(f"./src/{msg.identifier}.py", "w") as file:
        _ = file.write(buffer)


if __name__ == "__main__":
    main()
