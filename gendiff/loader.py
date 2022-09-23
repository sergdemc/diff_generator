import os
from gendiff.parser import parse_file


def load_file(pathfile: str) -> dict:
    extension = os.path.splitext(pathfile)[1].lstrip('.')
    return parse_file(open(pathfile), extension)
