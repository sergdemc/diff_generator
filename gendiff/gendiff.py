from gendiff import cli
import json

path1, path2 = cli.parse_cli()


def parse_file(path: str):
    with open(path) as f:
        return json.load(f)


def to_json_format(value: (bool, None)):
    if value is None:
        return 'null'
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    return value


def generate_diff(path1: str, path2: str):
    file1 = parse_file(path1)
    file2 = parse_file(path2)
    keys = list(set(file1.keys()) | set(file2.keys()))
    res = '{'
    for key in sorted(keys):
        if file1.get(key) == file2.get(key):
            res += f"\n   {key}: {to_json_format(file1[key])}"
        elif key in file1.keys() and key not in file2.keys():
            res += f"\n - {key}: {to_json_format(file1[key])}"
        elif key in file2.keys() and key not in file1.keys():
            res += f"\n + {key}: {to_json_format(file2[key])}"
        elif key in file1.keys() and key in file2.keys():
            res += f"\n - {key}: {to_json_format(file1[key])}"
            res += f"\n + {key}: {to_json_format(file2[key])}"
    res += '\n}'
    return res
