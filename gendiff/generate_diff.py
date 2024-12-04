import json

import yaml

from gendiff.formatters import plain, stylish


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

def generate_diff(file_path1, file_path2, format_type='stylish'):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)
    diff = build_diff(data1, data2)

    if format_type == 'plain':
        return plain.plain(diff)
    elif format_type == 'stylish':
        return stylish.stylish(diff)
