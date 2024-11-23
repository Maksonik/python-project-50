import pytest


@pytest.fixture
def file_1():
    return "./files/file1.json"

@pytest.fixture
def file_some_1():
    return "./files/file1.json"

@pytest.fixture
def file_2():
    return "./files/file2.json"
