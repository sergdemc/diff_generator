import json

from gendiff.formatters.normalize import normalize_values


def format(diff: dict) -> str:
    """
    Main func for json-like format output.
        diff (dict): dict with differences
        return: json-like string
    """
    diff = normalize_values(diff)
    return json.dumps(diff, indent=4)
