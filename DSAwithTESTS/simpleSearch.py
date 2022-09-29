#search for a key in a array

def searchForKey(array_, key):
    for k in range(0, len(array_)):
        if key == array_[k]:
            print(f'The {key} is found at {k}')
            return k
        
    print(f'The {key} is not found')
    
    return -1

test = [24, 4,3,5,1556,16,15,9]
print(searchForKey(test, 5))
print(searchForKey(test, 59))


def simpleBinarySearch(myList, key):
    
    low = 0
    high = len(myList) - 1
    mid = (low + high) // 2
    while low < high:
        
        if myList[mid] == key:
            print(f'The {key} is found at {mid}')
            break
        elif myList[mid] < key:
            low = mid + 1
        elif myList[mid] > key:
            low = mid - 1
    print(f'The {key} is not found')
    
simpleBinarySearch(test, 5)

matrix = [[1,2,3],[4,5,6],[7,8,9]]

add  = 0

for k in range(0, len(matrix)):
    for m in range(len(matrix[k])):
        add += matrix[k][m]
        
print(add)


def fibonacci(number):
    if number < 0 or int(number ) != number:  #negative numbers
        return "Not defined"
    
    if number == 0 or number == 1:
        return number
    else:
        fib = fibonacci(number - 1) + fibonacci(number - 2)
        print(fib)
        return fib
    
    
def printPairs(array):
    for i in array:
        for j in array:
            print(str(i) + " " + str(j))
            
# printPairs([1,2,3,4,5,6,7,8,9])

def unorderedPairs(array):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            print(array[i], array[j])
    
    
unorderedPairs([1,2,3,4,5,6,7,8,9])

