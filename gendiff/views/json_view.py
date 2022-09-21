import json


def view_diff(diff: dict) -> str:
    return json.dumps(diff, indent=4)
