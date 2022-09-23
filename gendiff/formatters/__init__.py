from gendiff.formatters import stylish, plain, json_format

RENDERS = {
    'stylish': stylish,
    'plain': plain,
    'json': json_format
}


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
