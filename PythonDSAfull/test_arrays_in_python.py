from ArraysInPython import create_array,insertIntoArray,traverseArray,get_element,searchForElement

def test_arrays_in_python():
    assert create_array(8)

def test_insert():
    assert insertIntoArray(0, 90, [9,3,4,1,3,5]) #O(1)
    assert insertIntoArray(-1, 90, [9,3,4,1,3,5]) #O(1)
    assert insertIntoArray(3, 90, [9,3,4,1,3,5])#O(N)
    assert insertIntoArray(8, 90, [9,3,4,1,3,5])#O(N)


def test_traverse():
    assert traverseArray([9,3,4,1,3,5])
    assert traverseArray([8])
    assert traverseArray([])

def test_getelement():
    assert get_element(3, [9,3,4,1,3,5])
    assert get_element(0, [9,3,4,1,3,5])
    assert get_element(10, [9,3,4,1,3,5])
    assert get_element(-1, [9,3,4,1,3,5])
    assert get_element(3, [])

def test_search_for_element():
    assert searchForElement(3, [9,3,4,1,3,5])
    assert searchForElement(3, [])
    assert searchForElement(3, [9,4,1,5])
    assert searchForElement(3, [3])