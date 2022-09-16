
def stringify_val(data, depth: int) -> str:
    if not isinstance(data, dict):
        return data
    tmp = ["{"]
    for k, v in data.items():
        tmp.append(f"\n{'  '*depth}  {k}: {stringify_val(v, depth+2)}")
    tmp.append(f"\n{'  '*(depth-1)}}}")
    return ''.join(tmp)


def stringify_diff(file: dict, depth=1) -> str:
    lst = []
    for k, v in file.items():
        if v['flag'] == 'nested':
            lst.append(f"{'  '*depth}  {k}: {{\n")
            lst.append(f"{stringify_diff(v['value'], depth + 2)}")
            lst.append(f"{'  '*(depth+1)}}}\n")
        elif v['flag'] == 'changed':
            lst.append(f"{'  '*depth}- {k}: "
                       f"{stringify_val(v['old_value'], depth+2)}\n")
            lst.append(f"{'  ' * depth}+ {k}: "
                       f"{stringify_val(v['new_value'], depth+2)}\n")
        elif v['flag'] == 'unchanged':
            lst.append(f"{'  ' * depth}  {k}: "
                       f"{stringify_val(v['value'], depth+2)}\n")
        elif v['flag'] == 'added':
            lst.append(f"{'  ' * depth}+ {k}: "
                       f"{stringify_val(v['value'], depth+2)}\n")
        elif v['flag'] == 'removed':
            lst.append(f"{'  ' * depth}- {k}: "
                       f"{stringify_val(v['value'], depth+2)}\n")
    res = ''.join(lst)
    return res


def final_stringify_diff(file: dict) -> str:
    return f"{{\n{stringify_diff(file)}}}"


# d1 = {
#   "common": {
#     "setting1": "Value 1",
#     "setting2": 200,
#     "setting3": True,
#     "setting6": {
#       "key": "value",
#       "doge": {
#         "wow": ""
#       }
#     }
#   },
#   "group1": {
#     "baz": "bas",
#     "foo": "bar",
#     "nest": {
#       "key": "value"
#     }
#   },
#   "group2": {
#     "abc": 12345,
#     "deep": {
#       "id": 45
#     }
#   }
# }
#
# d2 = {
#   "common": {
#     "follow": False,
#     "setting1": "Value 1",
#     "setting3": None,
#     "setting4": "blah blah",
#     "setting5": {
#       "key5": "value5"
#     },
#     "setting6": {
#       "key": "value",
#       "ops": "vops",
#       "doge": {
#         "wow": "so much"
#       }
#     }
#   },
#   "group1": {
#     "foo": "bar",
#     "baz": "bars",
#     "nest": "str"
#   },
#   "group3": {
#     "deep": {
#       "id": {
#         "number": 45
#       }
#     },
#     "fee": 100500
#   }
# }
