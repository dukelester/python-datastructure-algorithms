#Given an Array of integers, return an Array where every element at an even-indexed position is squared.

def evenElements(arr):
    
    for i in range(len(arr)):
        if i % 2 == 0:
            arr[i] *= arr[i]
    print(arr)
evenElements([9, 78, 90, 67, 5, 98])
            
            