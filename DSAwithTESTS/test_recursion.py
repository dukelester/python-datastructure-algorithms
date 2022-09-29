from .recursion import (factorialOfNumber,fibonacciOfNumber,findPower,findGCD,decimalToBinary,
                        reverseList,reverseString)

import pytest
def test_factorial():
    print(factorialOfNumber(8))
    assert factorialOfNumber(8)
    assert factorialOfNumber(-8)
    assert factorialOfNumber(0)
    
def test_fibonacci():
    print(fibonacciOfNumber(9), '================')
    assert fibonacciOfNumber(9)
    
def test_findPower():
    assert findPower(34, 22)
    assert findPower(2, 3) == 8
    
def test_findGCD():
    assert findGCD(60, 36)
    assert findGCD(12, 4)
    
def test_decimalToBinary():
    assert decimalToBinary(10) == 1010
    assert decimalToBinary(67) == 1000011
    assert decimalToBinary(0) == 0
    assert decimalToBinary(78.567890)
    

def test_reverseList():
    my_list = [1,2,3,4,5]
    assert reverseList(my_list,0, len(my_list) ) 
    
def test_reverseString():
    assert reverseString("duke lester")
    assert reverseString("Lester lester here at lester")
    