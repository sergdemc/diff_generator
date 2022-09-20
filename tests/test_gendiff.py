import pytest
from gendiff import gen_diff

json_1 = "tests/fixtures/file1.json"
json_2 = "tests/fixtures/file2.json"
res_stylish = "tests/fixtures/result_stylish"
yaml_1 = "tests/fixtures/file1.yml"
yaml_2 = "tests/fixtures/file2.yaml"
res_plain = "tests/fixtures/result_plain"

formats = ['stylish', 'plain', 'json']


@pytest.mark.parametrize('path1, path2, format_name, expected', [(json_1, json_2, formats[0], res_stylish),
                                                                 (yaml_1, yaml_2, formats[0], res_stylish),
                                                                 (json_1, json_2, formats[1], res_plain),
                                                                 (yaml_1, yaml_2, formats[1], res_plain)])
def test_generate_diff(path1, path2, format_name, expected):
    with open(expected) as f:
        assert gen_diff.generate_diff(path1, path2, format_name) == f.read()

# def test_with_empty_file():
#     with pytest.raises(json.JSONDecodeError):
#         generate_diff(json_1, empty_file)
