import pytest

class TestClass:

    def test_methodA(self):
        print("Run test Method A.....")
        assert True

    def test_methodB(self):
        print("Run test Method B.....")
        assert True
    pytest.mark.run(order=1)
    def test_methodC(self):
        print("Run test Method C.....")
        assert True

    def test_methodD(self):
        print("Run test Method D.....")
        assert True

    pytest.mark.run(order=2)
    def test_methodE(self):
        print("Run test Method E.....")
        assert True

    def test_methodF(self):
        print("Run test Method F.....")
        assert True