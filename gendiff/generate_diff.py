import json

import yaml


def read_file(file_path):
    with open(file_path) as file:
        if file_path.endswith(('.yaml', '.yml')):
            return yaml.load(file, Loader=yaml.CLoader)
        elif file_path.endswith('.json'):
            return json.load(file)
    raise ValueError("Unsupported file format")


def build_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    diff = {}
    for key in keys:
        if key not in data1:
            diff[key] = {"status": "added", "value": data2[key]}
        elif key not in data2:
            diff[key] = {"status": "removed", "value": data1[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {"status": "nested", "children": build_diff(data1[key], data2[key])}
        elif data1[key] != data2[key]:
            diff[key] = {"status": "changed", "old_value": data1[key], "new_value": data2[key]}
        else:
            diff[key] = {"status": "unchanged", "value": data1[key]}
    return diff


def format_stylish(diff, depth=0):
    indent = " " * (depth * 4)
    child_indent = " " * ((depth + 1) * 4)
    lines = []

    status_actions = {
        "added": lambda k, v: f"{indent}  + {k}: {format_value(v['value'], depth + 1)}",
        "removed": lambda k, v: f"{indent}  - {k}: {format_value(v['value'], depth + 1)}",
        "changed": lambda k, v: (
            f"{indent}  - {k}: {format_value(v['old_value'], depth + 1)}\n"
            f"{indent}  + {k}: {format_value(v['new_value'], depth + 1)}"
        ),
        "nested": lambda k, v: f"{indent}    {k}: {{\n{format_stylish(v['children'], depth + 1)}\n{child_indent}}}",
        "unchanged": lambda k, v: f"{indent}    {k}: {format_value(v['value'], depth + 1)}",
    }

    for key, value in diff.items():
        lines.append(status_actions[value["status"]](key, value))

    return "\n".join(lines)


def format_value(value, depth):
    if isinstance(value, dict):
        indent = " " * (depth * 4)
        child_indent = " " * ((depth + 1) * 4)
        lines = [f"{child_indent}{k}: {format_value(v, depth + 1)}" for k, v in value.items()]
        return f"{{\n{'\n'.join(lines)}\n{indent}}}"
    return json.dumps(value)


def generate_diff(file_path1, file_path2):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)
    diff = build_diff(data1, data2)
    return f"{{\n{format_stylish(diff)}\n}}".replace('"', '')
