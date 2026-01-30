import pytest

@pytest.fixture()
def setup():
    print("launch the browser...")
    yield
    print("close the browser...")