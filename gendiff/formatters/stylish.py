import json


def format_value(value, depth):
    """Форматирует значения для отображения в стильном формате."""
    if isinstance(value, dict):
        indent_size = 4
        current_indent = " " * (depth * indent_size)
        next_indent = " " * ((depth + 1) * indent_size)
        lines = [f"{next_indent}{key}: {format_value(val, depth + 1)}" for key, val in value.items()]
        return f"{{\n{'\n'.join(lines)}\n{current_indent}}}"
    return json.dumps(value)


def format_stylish(diff, depth=0):
    """Рекурсивно форматирует различия для вывода в стильном формате."""
    indent_size = 4
    current_indent = " " * (depth * indent_size)
    next_indent = " " * ((depth + 1) * indent_size)
    lines = []

    for key, value in diff.items():
        status = value["status"]

        if status == "added":
            lines.append(f"{current_indent}  + {key}: {format_value(value['value'], depth + 1)}")
        elif status == "removed":
            lines.append(f"{current_indent}  - {key}: {format_value(value['value'], depth + 1)}")
        elif status == "changed":
            lines.append(f"{current_indent}  - {key}: {format_value(value['old_value'], depth + 1)}")
            lines.append(f"{current_indent}  + {key}: {format_value(value['new_value'], depth + 1)}")
        elif status == "nested":
            children = format_stylish(value["children"], depth + 1)
            lines.append(f"{current_indent}    {key}: {{\n{children}\n{next_indent}}}")
        elif status == "unchanged":
            lines.append(f"{current_indent}    {key}: {format_value(value['value'], depth + 1)}")

    return "\n".join(lines)


def stylish(diff):
    """Возвращает строку с разницей в стильном формате."""
    return f"{{\n{format_stylish(diff)}\n}}".replace('"', '')
