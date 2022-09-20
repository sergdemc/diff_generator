import json
import yaml


def parse_json(path: str):
    return json.load(open(path))


def parse_yaml(path: str):
    return yaml.safe_load(open(path))


def get_dict(path: str) -> dict:
    """
    Read yml or json file and return dict.
    """
    if isinstance(path, str):
        if path.endswith('.json'):
            return parse_json(path)
        elif path.endswith('.yaml') or path.endswith('.yml'):
            return parse_yaml(path)


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
