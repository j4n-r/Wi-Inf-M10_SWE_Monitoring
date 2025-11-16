import time
from typing import Any
from generator.msg_out import (
    AccelStampedMessage,
    Vector3Message,
    HeaderMessage,
    AccelMessage,
)
from dataclasses import asdict

points = {
    "measurement": "home",
    "tags": {"room": "Kitchen", "sensor": "K001"},
    "fields": {"temp": 72.2, "hum": 36.9, "co": 4},
    "time": 1762545600,
}


# {'linear': {'x': 2, 'y': 3, 'z': 1}, 'angular': {'x': 2, 'y': 3, 'z': 1}}
# {'linear_x': 2, 'linear_y': 3, 'linear_z': 1, 'angular_x': 2, 'angular_y': 3, 'angular_z': 1}

vec1 = Vector3Message(2, 3, 1)
vec2 = Vector3Message(3, 3, 3)
header = HeaderMessage(1, 122135532, "frameid")
acc_msg = AccelMessage(vec1, vec2)
msg = AccelStampedMessage(header, acc_msg)


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


items = flatten_message(asdict(msg), "")

point = {
    "measurement": str(msg.__class__.__name__),
    "tags": "",
    "fields": items,
    "time": int(time.time()),
}

print(point)
print(asdict(msg))
# print(items)
print(items)
