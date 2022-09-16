import pytest
from gendiff import generate_diff


json_1 = "tests/fixtures/file1.json"
json_2 = "tests/fixtures/file2.json"
json_res_1 = "tests/fixtures/result1_json"
json_res_2 = "tests/fixtures/result2_json"
empty_file = "tests/fixtures/file_empty"
empty_json = "tests/fixtures/empty_json.json"
yaml_1 = "tests/fixtures/file1.yml"
yaml_2 = "tests/fixtures/file2.yaml"
empty_yml = "tests/fixtures/empty_yml.yml"
yml_res_1 = "tests/fixtures/result1_yml"
yml_res_2 = "tests/fixtures/result2_yml"


@pytest.mark.parametrize('path1, path2, expected', [(json_1, json_2, json_res_1),
                                                    (yaml_1, yaml_2, yml_res_1)])
def test_generate_diff(path1, path2, expected):
    with open(expected) as f:
        assert generate_diff.generate_diff(path1, path2) == f.read()



# def test_with_empty_file():
#     with pytest.raises(json.JSONDecodeError):
#         generate_diff(json_1, empty_file)

