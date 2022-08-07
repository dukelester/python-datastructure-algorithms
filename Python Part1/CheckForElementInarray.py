from unittest import result


def checkForElement(arr, element):
    
    if len(arr) == 0:
        return -1
    for i in arr:
        # print(i)
        if i == element:
            return True
    return False
       
       
        
result = checkForElement([23,434,44,56,6,7,88,9,90], 9)
result = checkForElement([], 9)
print(result)