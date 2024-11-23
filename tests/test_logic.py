from gendiff import generate_diff


def test_logic_json_some(file_1_json, file_some_1_json):
    result = generate_diff(file_1_json, file_some_1_json)

    assert "+" not in result and "-" not in result


def test_logic_json_not_some(file_1_json, file_2_json):
    result = generate_diff(file_1_json, file_2_json)

    assert "+" in result or "-" in result


def test_logic_yml_some(file_1_yml, file_some_1_yml):
    result = generate_diff(file_1_yml, file_some_1_yml)

    assert "+" not in result and "-" not in result


def test_logic_yml_not_some(file_1_yml, file_2_yml):
    result = generate_diff(file_1_yml, file_2_yml)

    assert "+" in result or "-" in result
