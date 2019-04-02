import pytest
from src.pictotxt import test

def test_test():
    assert test() == 7

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4
