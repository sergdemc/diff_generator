import json


def parse_file(path: str):
    with open(path) as f:
        return json.load(f)


def to_json_format(value: (bool, None)):
    diffs = {None: 'null', True: 'true', False: 'false'}
    if value in diffs:
        return diffs[value]
    return value


def generate_diff(first: str, second: str):
    file1 = parse_file(first)
    file2 = parse_file(second)
    keys = list(set(file1.keys()) | set(file2.keys()))
    res = '{'
    for key in sorted(keys):
        if file1.get(key) == file2.get(key):
            res += f"\n    {key}: {to_json_format(file1[key])}"
        elif key in file1.keys() and key not in file2.keys():
            res += f"\n  - {key}: {to_json_format(file1[key])}"
        elif key in file2.keys() and key not in file1.keys():
            res += f"\n  + {key}: {to_json_format(file2[key])}"
        elif key in file1.keys() and key in file2.keys():
            res += f"\n  - {key}: {to_json_format(file1[key])}"
            res += f"\n  + {key}: {to_json_format(file2[key])}"
    res += '\n}'
    return res
