import pytest

@pytest.fixture()
def setup():
    print("launching the browser....")
    driver = webdriver.Chrome()