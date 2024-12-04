from gendiff import generate_diff


def test_logic_json_some(file_1_json, file_some_1_json):
    result = generate_diff(file_1_json, file_some_1_json)

    assert "+" not in result and "-" not in result


def test_logic_json_not_some(file_1_json, file_2_json):
    result = generate_diff(file_1_json, file_2_json)

    assert "+" in result or "-" in result
    print(result)
    print()
    assert result == """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""


def test_logic_yml_some(file_1_yml, file_some_1_yml):
    result = generate_diff(file_1_yml, file_some_1_yml)

    assert "+" not in result and "-" not in result


def test_logic_yml_not_some(file_1_yml, file_2_yml):
    result = generate_diff(file_1_yml, file_2_yml)

    assert "+" in result or "-" in result
