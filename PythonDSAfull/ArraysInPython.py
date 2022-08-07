#contiguous memory ==> elements of the same type ==> sequentially
#1 Dimension arrays and multidimensional arrays 
#1 Dimensional array == linear array ==> each element has a single index value  => one row but multiple columns
#size of the array in memory = number of elements  x 4 bytes eg 10 x 4 = 40

'''
2Dimensional Array

combination of 1 D array 
element are accessed by two indeces
array[i][j]  = element

3D --> elements are accessed by 3 indeces ==> array[i][j][k]

from array import array, array, array, array, array, array, array, array, *

myarray = array(type_data, [initialization])


'''
from array import *

int_arr =  array('i', [23,5,6,7,9,00,5]) #O(1) time of creating an array while space is O(N)

double_arr = array('d', [34.678, 445.78,98.4567,223.98,33.67890]) #O(1) time of creating an array space is O(N)
print(int_arr,double_arr)


def create_array(length):
    data = array('i', [ ]) #create an empty array
    length = eval(input("Enter the length of the array:  \t"))
    if length < 0:
        print("The length must be bigger than 0")
        return -1

    if length == 0:
        print("The length must be positive")
        return -1
    
    elif int(length) != length:
        print("The length must be positive whole number (integer)")
        length = eval(input("Enter the a positive integer as length for the array:  \t"))

    else :
        for i in range(length):
            value = eval(input("Enter a value for the array: \t"))
            data.append(value)
    print(data)
    return data


#insert element into an array using the insert(index, element)

def insertIntoArray(index, element, data):
    data.insert(index, element)
    print(data)
    return data

def traverseArray(arr):
    if len(arr) == 0:
        return -1
    elif len(arr) == 1:
        return arr[0]
    else:
        for element in arr:  # time complexity O(1) space complexity  is O(1)
            print(element)
        return element

def get_element(index, arr):
    if index >= len(arr):
        print("Element not found at index")
        return -1
    else:
        print("found", arr[index])
        return arr[index] #O(1) time complexity O(1) space complexity


def searchForElement(element, data_array):
    if element is None:
        return -1
    if len(data_array) == 1:
        return data_array[0]

    if len(data_array) == 0:
        return -1
    
    else:
        for i in range(len(data_array)):
            if data_array[i] == element:
                print(i, 'found here ')
                return i
            else:
                return -1


def searchIn2D(arr, key):
    for i in range(len(arr)):
        for p in range(len(arr[0])):
            if arr[i][p] == key:
                print('found at', i, p )


searchIn2D([[22,3,4,62,2,5], [83,3,5,1,4,1], [90,3,4,1,5,11,45,9]], 90)

        


