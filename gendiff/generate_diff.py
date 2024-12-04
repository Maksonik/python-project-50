from gendiff.build_diff import build_diff, read_file
from gendiff.formatters import plain, stylish, json


def generate_diff(file_path1, file_path2, format_type='stylish'):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)
    diff = build_diff(data1, data2)

    if format_type == 'plain':
        return plain.plain(diff)
    elif format_type == 'json':
        return json.json_format(diff)
    return stylish.stylish(diff)
