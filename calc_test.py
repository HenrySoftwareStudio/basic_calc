# I know import * is bad convention, but I'm not sure how to do it better
# without listing all the functions in calc.py and having a super long line
from calc import *
# TODO: finish adding tests for all major functions in calc.py
# test suite below
def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(1, -1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(5, -3) == 8
    assert subtract(-4, 3) == -7
    assert subtract(-4, -3) == -1
    assert subtract(0, 0) == 0
    assert subtract(0, -1) == 1

def test_multiply():
    assert multiply(5, 3) == 15
    assert multiply(5, -3) == -15
    assert multiply(-4, 0) == 0
    assert multiply(3, 0) == 0
    assert multiply(0, 0) == 0
    assert multiply(-1, -5) == 5

def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
    assert divide(-10, 2) == -5
    assert divide(-5, 5) == -1
    assert divide(0, 1) == 0