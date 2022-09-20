
def corr_vals(data):
    """
    Return '[complex value]' if dict value is complex,
    otherwise return data.
    :param data: dict value
    :return: '[complex value]' or argument data
    """
    if isinstance(data, (list, set, tuple, dict)):
        return '[complex value]'
    elif data in ('true', 'false', 'null'):
        return data
    return f"'{data}'"


def gen_plain_diff(diff: dict, keys=None) -> list:
    if keys is None:
        keys = []
    res = []
    for k, v in diff.items():
        flag = v['flag']
        keys.append(str(k))
        path = '.'.join(keys)
        if flag == 'nested':
            res.extend(gen_plain_diff(v['value'], keys))
            keys = keys[:-1]
        else:
            val = v.get('value')
            old_val = v.get('old_value')
            new_val = v.get('new_value')
            msgs = {
                'unchanged': '',
                'removed': f"Property '{path}' was removed",
                'added':
                    f"Property '{path}' was added with value: {corr_vals(val)}",
                'changed': f"Property '{path}' was updated. "
                    f"From {corr_vals(old_val)} to {corr_vals(new_val)}"
            }
            res.append(msgs.get(flag))
        keys = keys[:-1]
    return res


def view_diff(diff: dict) -> str:
    diff = gen_plain_diff(diff)
    return '\n'.join(filter(lambda s: s != '', diff))
