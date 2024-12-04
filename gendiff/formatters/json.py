import json


def json_format(diff):
    """Возвращает разницу между двумя объектами в формате JSON."""
    return json.dumps(diff, indent=4)