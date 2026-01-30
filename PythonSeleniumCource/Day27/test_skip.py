import pytest

class TestClass:
    def test_loginByEmail(self):
        print("login by email...")
        assert True

    def test_loginByFacebook(self):
        print("login by facebook...")
        assert True

    @pytest.mark.skip(reason="skip test")
    def test_loginByInstagram(self):
        print("login by instagram...")
        assert True

    def test_loginByTwitter(self):
        print("login by twitter...")
        assert True

    def test_SignUpByTwitter(self):
        print("Sign up by twitter...")
        assert True

    @pytest.mark.skip(reason="skip test")
    def test_SignUpByInstagram(self):
        print("Sign up by instagram...")
        assert True
