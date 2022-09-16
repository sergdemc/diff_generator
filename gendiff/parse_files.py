import json
import yaml


def parse_json(path: str):
    try:
        return json.load(open(path))
    except json.JSONDecodeError:
        return {}


def parse_yaml(path: str):
    f = yaml.safe_load(open(path))
    if f:
        return f
    return {}


def get_dict(path: str) -> dict:
    """
    Read yml or json file and return dict.
    """
    if isinstance(path, str):
        if path.endswith('.json'):
            return parse_json(path)
        elif path.endswith('.yaml') or path.endswith('.yml'):
            return parse_yaml(path)
        else:
            raise ValueError("Input path to json or yml files")
    else:
        raise ValueError("Input path as string")


def normalize_values(file: dict) -> dict:
    """
    Changes bool types and None type values:
        True to 'true', False to 'false', None to 'null'.
    """
    corr_values = {True: 'true', False: 'false', None: 'null'}

    for key, val in file.items():
        if isinstance(val, dict):
            normalize_values(val)
        elif val in corr_values:
            file[key] = corr_values[val]
    return file
