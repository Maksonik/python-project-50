def format_value(value):
    if isinstance(value, dict) or isinstance(value, list):
        return "[complex value]"
    elif value is None:
        return "null"
    elif isinstance(value, int):
        return str(value)
    return f"'{str(value)}'"


def format_diff(diff, parent=''):
    lines = []
    for key, value in diff.items():
        full_key = f"{parent}.{key}" if parent else key
        status = value["status"]

        if status == "added":
            lines.append(f"Property '{full_key}' was added with value: {format_value(value['value'])}")
        elif status == "removed":
            lines.append(f"Property '{full_key}' was removed")
        elif status == "changed":
            lines.append(
                f"Property '{full_key}' was updated. From {format_value(value['old_value'])}"
                f" to {format_value(value['new_value'])}")
        elif status == "nested":
            lines.append(format_diff(value["children"], full_key))
        elif status == "unchanged":
            continue
    return "\n".join(lines)


def plain(diff):
    return format_diff(diff)
