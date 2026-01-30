import pytest

class TestClass:

    @pytest.fixture()   #decorator...
    def setup(self):
        print("Open the application...")
        yield
        print("closing browser...")

    def test_Login(self,setup):
        print("Perform login test")

    def test_Search(self,setup):
        print("Perform Search test")

    def test_Advancesearch(self,setup):
        print("Perform advanced search test")