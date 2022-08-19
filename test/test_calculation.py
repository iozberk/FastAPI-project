from app.calculation import add, subtract, multiply, divide
from pytest import mark

# Pytest will run this test first because it is marked with the @mark.parametrize decorator
@mark.parametrize("num1, num2, result", [
    (3, 2, 5),
    (7, 1, 8),
    (12, 4, 16),
    (5, 5, 10)])
def test_add(num1, num2, result):
    assert add(num1, num2) == result


# def test_add(num1, num2, result):
#     assert add(1, 1) == 2
#     assert add(1, 2) == 3
#     assert add(2, 2) == 4

def test_subtract():
    assert subtract(9, 4) == 5


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(20, 5) == 4
