from gendiff import generate_diff


def test_logic_some(file_1, file_some_1):
    result = generate_diff(file_1, file_some_1)

    assert "+" not in result and "-" not in result


def test_logic_not_some(file_1, file_2):
    result = generate_diff(file_1, file_2)

    assert "+" in result or "-" in result

