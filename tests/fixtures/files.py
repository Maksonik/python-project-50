import pytest


@pytest.fixture
def file_1_json():
    return "./files/file1.json"


@pytest.fixture
def file_some_1_json():
    return "./files/file1.json"


@pytest.fixture
def file_2_json():
    return "./files/file2.json"


@pytest.fixture
def file_1_yml():
    return "./files/file1.yml"


@pytest.fixture
def file_some_1_yml():
    return "./files/file1.yml"

@pytest.fixture
def file_2_yml():
    return "./files/file2.yml"
