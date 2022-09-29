'''
Inbuilt data structures which store sequence of data items
can hold elements of different types.
mutable, ordered and allow duplicates.
'''

my_list = [] #!empty list
my_list = [9,6,33,45,45]
#list[index] ==> gets an element from a list
my_list.sort(reverse=True)
print(my_list)
print(my_list.count(45))
my_list.reverse()
print(my_list)

name = "Duke Lester"

name_list = list(name)
print(name_list)

#!interview questions for lists
def findMissing(my_list):
    N = len(my_list) + 1
    sum_of_nums = N * (N + 1) // 2
    sum_list = sum(my_list)
    missing_number = sum_of_nums - sum_list
    return missing_number

print(findMissing([1,4,5,7,8,9,3]))

def sumOfDigits(my_list, target):
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            print(j)
            if my_list[i] == my_list[j]:
                continue
            elif my_list[i] + my_list[j] == target:
                print('found')
                return (my_list[i] , my_list[j]) 
    
print(sumOfDigits([1,4,5,7,8,9,3], 15))
print(sumOfDigits([1,4,5,7,8,9,3], 10))
print(sumOfDigits([1,4,5,7,8,9,3], 5))


def maximumProduct(my_list):
    maximum_prod = 0
    for k in range(len(my_list)):
        for j in range(k + 1, len(my_list)):
            if my_list[k] * my_list[j] > maximum_prod:
                maximum_prod = my_list[k] * my_list[j]
                pairs = (my_list[k] , my_list[j])
    return maximum_prod, pairs
print('')           
print(maximumProduct([1,4,5,7,8,9,3]))
print(maximumProduct([9,67, 8, 90, 45, 55]))


def checkIfUnique(my_list):
    visted =[]
    
    for i in my_list:
        if i in visted:
            return False
        else:
            visted.append(i)
    return True
print(checkIfUnique([1,4,5,7,8,9,3]))
print(checkIfUnique([1,5,4,4,5,7,8,9,3]))


def isPermutation(list_1, list_2):
    list_1.sort()
    list_2.sort()
    if len(list_2) == len(list_1) and list_2 == list_1:
        return True
    else:
        return False
    
print(isPermutation([1,4,5,7,8,9,3], [1,4,5,7,8,9,3]))
print(isPermutation([78,4,5,7,8,9,3], [1,4,5,7,8,9,3, 78]))
    
    
def isBiggerThanAvg(marks):
    count = 0
    average = sum(marks)/ len(marks)
    print('average is ', average)
    for m in marks:
        if m > average:
            count += 1
        else:
            continue
    return count
print(isBiggerThanAvg([1,4,5,7,8,9,3]))

my_list = [1,4,5,7,8,9,3]
print(my_list[1:len(my_list) -1])

def sumDiagonal(my_list):
    sum = 0
    for i in range(len(my_list)):
        sum += my_list[i][i]
    return sum

print(sumDiagonal([
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]))
print(' '.join(['hello','duke','lester','come','here']))
import random
print("duke lester is a pro programmers".split())
lester = "duke lester is a pro programmers".split()
random.shuffle(lester)
print(lester)
print([ i.split('e') for i in lester ])


numbers = '234 56 78 900 98 76 54'
numbers = numbers.split()
print(numbers)
for number in range(0, len(numbers)):
    numbers[number] = int(numbers[number])
print(numbers, sum(numbers))
    
x = next(iter(numbers))
print(x)

print(*numbers, sep=" " )
print(*[9, 7, 'duke', 'lester'], sep=' ')

li = [1,2,3,4,5,6,7,8,9,10]
obj = enumerate(li) #add index to each element in the list
print(list(obj))


