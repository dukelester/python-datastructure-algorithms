from unittest import result


def checkMountainArray(arr):
    is_increasing = True # the mountain has to start increasing
    
    if len(arr) < 0 or arr[1] < arr[0]:   #handling edge cases
        return False
    for i in range(len(arr) - 1):
        if arr[i + 1] == arr[i]:  # if any two elements are same, return False
            return False
        elif is_increasing and arr[i+1] < arr[i]:     # check if we observe a decrease while increasing and set flag
                is_increasing = False
        elif not is_increasing and arr[i+1] > arr[i]: # check if we observe a decrease while increasing
            return False                              # since this mean we go up and down more than once, return False
        return not is_increasing                          # handling edge case where mountain always increase
        
            

result = checkMountainArray([2,1])
print(result)
                
    