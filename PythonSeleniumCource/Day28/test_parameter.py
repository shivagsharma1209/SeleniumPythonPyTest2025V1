import pytest

class TestClass:
    @pytest.mark.parametrize('num1, num2',[(10,10),(2,5),(4,7),(23,45)])
    def test_calculation(selfself, num1, num2):
        assert num1 == num2
