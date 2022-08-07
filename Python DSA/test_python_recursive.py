from PythonRecursive import findFactorial,tailRecursion,treeRecursive,nestedFunction
import pytest

def test_factorial():
    print("Testing factorial and Recursiveness ")
    assert findFactorial(3) 
    assert findFactorial(1) 
    assert findFactorial(0) 
    assert findFactorial(-93) 
    assert findFactorial(10.562) 
    assert findFactorial(-10.562) 


def test_tail_recursion():
    assert tailRecursion(None)
    assert tailRecursion(8)

def test_treeRecursive():
    assert treeRecursive(0)
    assert treeRecursive(None)
    assert treeRecursive(9)

def test_nested_function():
    assert nestedFunction(7)
    assert nestedFunction(0)
    assert nestedFunction(None)

   