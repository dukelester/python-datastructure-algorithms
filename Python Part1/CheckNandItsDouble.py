def checkForDouble(arr):
    
    i = 0
    while i < len(arr):
        for j in range(0, len(arr)):
            if arr[j] == arr[i] and  i!=j:
                return True
        i += 1
    return False
        
            
solution = checkForDouble([9,6,3,2,8])
print(solution)