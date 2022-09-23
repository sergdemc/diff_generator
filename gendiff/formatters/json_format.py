import json


def format(diff: dict) -> str:
    """
    Main func for json-like format output.
        diff (dict): dict with differences
        return: json-like string
    """
    return json.dumps(diff, indent=4)
