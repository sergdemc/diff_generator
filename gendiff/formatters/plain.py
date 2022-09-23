def corr_vals(data):
    """
    Return '[complex value]' if dict value is complex,
    otherwise return data.
        data (Any): dict value
        return (Any): '[complex value]' or argument data
    """
    if isinstance(data, (list, set, tuple, dict)):
        return '[complex value]'
    elif data in ('true', 'false', 'null') or isinstance(data, (int, float)):
        return data
    return f"'{data}'"


msgs = {
    'unchanged': '',
    'removed': "Property '{path}' was removed",
    'added': "Property '{path}' was added with value: {val}",
    'changed': "Property '{path}' was updated. From {old_val} to {new_val}"
}


def gen_plain_diff(diff: dict, keys=None) -> list:
    """
    Generates list of strings with differences according dict msgs.
        diff (dict): dict with differences
        keys (None or list): list for accumulate strings
        return: list with accumulate strings
    """
    if keys is None:
        keys = []
    lines = []
    for k, v in diff.items():
        status = v['status']
        keys.append(str(k))
        path = '.'.join(keys)
        if status == 'nested':
            lines.extend(gen_plain_diff(v['value'], keys))
            keys = keys[:-1]
        else:
            val = corr_vals(v.get('value'))
            old_val = corr_vals(v.get('old_value'))
            new_val = corr_vals(v.get('new_value'))
            lines.append(msgs.get(status).format(
                path=path,
                val=val,
                old_val=old_val,
                new_val=new_val))
        keys = keys[:-1]
    return lines


def format(diff: dict) -> str:
    """
    Main func for plain format output.
        diff (dict): dict with differences
        return: str
    """
    diff = gen_plain_diff(diff)
    return '\n'.join(filter(lambda s: s != '', diff))
