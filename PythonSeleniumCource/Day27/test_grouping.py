import pytest
class TestClass:


    @pytest.mark.sanity
    def test_LoginByEmail(self):
        print("Login by Email.....")
        assert True

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_LoginByFacebook(self):
        print("Login by Facebook.....")
        assert True

    @pytest.mark.regression
    def test_LoginByTwitter(self):
        print("Login by Twitter.....")
        assert True

    @pytest.mark.regression
    def test_LoginByInstagram(self):
        print("Login by Instagram.....")
        assert True

    @pytest.mark.sanity
    def test_SignupByEmail(self):
        print("Signup by Email.....")
        assert True

    @pytest.mark.sanity
    def test_SignupByFacebook(self):
        print("Signup by Facebook.....")
        assert True

    @pytest.mark.regression
    def test_SignupByTwitter(self):
        print("Signup by Twitter.....")
        assert True

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_SignupByInstagram(self):
        print("Signup by Instagram.....")
        assert True


