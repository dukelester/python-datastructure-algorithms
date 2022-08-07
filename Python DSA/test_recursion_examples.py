
from RecursionExamples import fib,findFib
import pytest
def test_fib():
    assert fib (-34)
    assert fib(89.345672)
    # assert fib(0)
    assert fib(18)


def test_fib_2():
    assert findFib(9)
    assert findFib(-4)
    assert findFib(9.6789)
    assert findFib(1)
    assert findFib(0)
    
