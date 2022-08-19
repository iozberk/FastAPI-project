from app.calculation import add, subtract, multiply, divide

def test_add():
    assert add(1, 1) == 2
    assert add(1, 2) == 3
    assert add(2, 2) == 4


def test_subtract():
    assert subtract(9, 4) == 5


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(20, 5) == 4
