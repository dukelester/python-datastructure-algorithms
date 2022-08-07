"""
Given an array arr, replace every element in that array with
the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
"""

def replaceTheElements(arr):
    for i in range(len(arr)):
        if arr[i + 1] > arr[i]:
            arr[i] = arr[i + 1]
            arr[-1] = -1
    return arr

test = replaceTheElements([9,5,6,7,8,96,33])
print(test)
    