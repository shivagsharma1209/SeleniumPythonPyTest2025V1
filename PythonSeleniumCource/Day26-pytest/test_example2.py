import pytest

class TestClass:

    @pytest.fixture()   #decorator...
    def setup(self):
        print("pre-requisites...")
        print("Open the application...")

    def test_Login(self,setup):
        print("Login test")
    def test_Search(self,setup):
        print("Search test")
    def test_Advancesearch(self):
        print("Advanced search test")

