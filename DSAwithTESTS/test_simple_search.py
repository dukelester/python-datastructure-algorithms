import pytest

from . simpleSearch import searchForKey,simpleBinarySearch, fibonacci


def test_simpleSearch():
    assert searchForKey([24, 4,3,5,1556,16,15,9], 5) == 3
    assert searchForKey([24, 4,3,5,1556,16,15,9], 50)
    assert searchForKey([], 8)
    
# def test_simpleBinarySearch():
#     assert simpleBinarySearch([24, 4,3,5,1556,16,15,9], 3)
#     # assert simpleBinarySearch([24, 4,3,5,1556,16,15,9], 50, 0, len([24, 4,3,5,1556,16,15,9])-1)
#     # assert simpleBinarySearch([], 8, 0, len([])-1)
    
def test_fibonacci():
    assert fibonacci(5)
    assert fibonacci(20)
    assert fibonacci(-9)
    
    
    