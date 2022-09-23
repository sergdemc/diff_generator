import json
import yaml


formats = {
    'json': json.load,
    'yaml': yaml.safe_load,
    'yml': yaml.safe_load
}


def parse_file(file, extension: str) -> dict:
    """
    Read yaml or json file and return python dict.
        file (str): pathfile
        extension (str): json or yaml
        return (dict): python dictionary
    """
    if extension.lower() not in formats.keys():
        raise TypeError('Unsupported format. Follow formats are supported: {}'
                        .format(formats.keys()))
    return formats[extension.lower()](file)
