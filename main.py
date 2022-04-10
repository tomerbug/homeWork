import pytest


def add(num1, num2):
    return num1 + num2


# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2


# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2


# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2


# Function to divide evenlly two numbers
def diveideEvenlly(num1, num2):
    return num1 // num2


# Function to mudolo two numbers
def mudolo(num1, num2):
    return num1 % num2


print(mudolo(4, 4))
print(diveideEvenlly(4, 4))


# Function that gives the squre root of a number
def sqrt(num):
    sum= num ** (1 / 2)
    return sum


def test_add():
    assert 2 == add(1, 1)


def test_add2():
    assert 3 == add(2, 1)


def test_subtract():
    assert 5 == subtract(10, 5)


def test_subtract2():
    assert 6 == subtract(10, 5)


def test_multiply():
    assert 4 == multiply(2, 2)


def test_multiply2():
    assert 10 == multiply(8, 2)


def test_divide():
    assert 0 == divide(0, 0)


def test_divide2():
    assert 8 == divide(100, 2)


def diveideEvenlly():
    assert 4 == diveideEvenlly(2, 2)


def diveideEvenlly2():
    assert 5 == diveideEvenlly(6, 2)


def test_mudolo():
    assert 6 == mudolo(8, 7)


def test_mudolo2():
    assert 1 == mudolo(9, 9)


def test_sqrt(num):
    assert 3 == sqrt(9)


def test_sqrt2(num):
    assert 3 == sqrt(8)

