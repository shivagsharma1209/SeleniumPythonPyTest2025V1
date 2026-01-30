import pytest

class TestClass:

    @pytest.mark.dependency()
    def test_openApp(self):
        print("Open the application.....")
        assert True

    @pytest.mark.dependency(depends=["TestClass::test_openApp"])
    def test_login(self):
        print("login to the application.....")
        assert False

    @pytest.mark.dependency(depends=["TestClass::test_login"])
    def test_Search(self):
        print("Perform search.....")
        assert True

    @pytest.mark.dependency(depends=["TestClass::test_search"])
    def test_Advsearch(self):
        print("Perform Advsearch.....")
        assert True

    @pytest.mark.dependency(depends=["TestClass::test_login"])
    def test_logout(self):
        print("Log out the application.....")
        assert True