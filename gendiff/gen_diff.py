from collections import OrderedDict
from gendiff.formatters import RENDERS
from gendiff.loader import load_file


def normalize_values(file: dict) -> dict:
    """
    Changes bool types and None type values:
        True to 'true', False to 'false', None to 'null'.
    """
    corr_values = {True: 'true', False: 'false', None: 'null'}

    for key, val in file.items():
        if isinstance(val, dict):
            normalize_values(val)
        elif isinstance(val, (bool, type(None))):
            file[key] = corr_values[val]
    return file


def get_diff(old: dict, new: dict) -> OrderedDict:  # noqa
    """
    Compares two python dict and generates one common OrderDict with differences.  # noqa: E501
        old (dict): first dict
        new (dict): second dict
        return (OrderDict): OrderDict with differences
    """
    res = {}
    old_keys = set(old.keys()) - set(new.keys())
    for key in old_keys:
        res[key] = {'status': 'removed', 'value': old[key]}

    new_keys = set(new.keys()) - set(old.keys())
    for key in new_keys:
        res[key] = {'status': 'added', 'value': new[key]}

    for key in old.keys() & new.keys():
        old_val = old[key]
        new_val = new[key]
        if isinstance(old[key], dict) and isinstance(new[key], dict):
            res[key] = \
                {'status': 'nested', 'value': get_diff(old_val, new_val)}
        elif old_val == new_val:
            res[key] = \
                {'status': 'unchanged', 'value': old_val}
        elif old_val != new_val:
            res[key] = \
                {'status': 'changed', 'old_value': old_val, 'new_value': new_val}  # noqa: E501
    return OrderedDict(sorted(res.items()))


def generate_diff(path1: str, path2: str, format_name='stylish') -> str:
    """
    Main function - generate differences of two files, json or yaml.
        path1 (str): pathfile to first file
        path2 (str): pathfile to second file
        format_name (str): format output data, default=stylish
        return (str): depends on param "format_name"
    """
    file1 = load_file(path1)
    file2 = load_file(path2)
    diff = get_diff(file1, file2)
    diff = normalize_values(diff)
    return RENDERS[format_name].format(diff)
