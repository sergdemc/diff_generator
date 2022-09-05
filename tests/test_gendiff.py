import pytest
import json

from gendiff.gendiff import generate_diff

path1 = "tests/fixtures/file1.json"
path2 = "tests/fixtures/file2.json"
result1 = 'tests/fixtures/result1_json'
result2 = 'tests/fixtures/result2_json'
empty_file = "tests/fixtures/file_empty"
empty_json = 'tests/fixtures/empty_json.json'


@pytest.mark.parametrize('file1, file2, expected', [(path1, path2, result1),
                                                    (path1, empty_json, result2)])
def test_generate_diff(file1, file2, expected):
    with open(expected) as f:
        assert generate_diff(file1, file2) == f.read()


def test_with_empty_file():
    with pytest.raises(json.JSONDecodeError):
        generate_diff(path1, empty_file)
