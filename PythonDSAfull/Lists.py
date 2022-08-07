def findMissing(listy):
    N = len(listy) + 1
    #sum of N numbers =  N * (n-2) // 2

    sum1 = N*(N+1)//2
    print(sum1 , 'sum 1')

    sum2 = sum(listy) #the sum of elements in list
    print(sum2, 'sum 2')
    missing = sum1 - sum2
    print(missing)

    return missing

findMissing([9,4,5,6])
findMissing([1,4,3,5])


def findSum(my_list, target):
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] == my_list[j]:
                continue
            elif my_list[i]  + my_list[j]  == target:
                print(i , j , 'found', my_list[i], my_list[j])

findSum([1,4,6,8,3,5,7,2], 5)


#maximum product pair in a list

def maximumProduct(my_list):
    maximum_prod = 0
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] * my_list[j] > maximum_prod:
                maximum_prod = my_list[i] * my_list[j]
                pairs = str(my_list[i]) + ',' + str(my_list[j])

    print(pairs)

maximumProduct([1,4,6,8,3,5,7,2])

def maximumSum(my_list):
    maximum_sum = 0
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] + my_list[j] > maximum_sum:
                maximum_sum = my_list[i] +  my_list[j]
                pairs = str(my_list[i]) + ',' + str(my_list[j])

    print(pairs)

maximumSum([1,4,6,8,3,5,7,2])



def isUnique(my_list_):
    visited = []
    for i in my_list_:
        if i in visited:
            return False
        else:
            visited.append(i)
    return True

print(isUnique([1,4,6, 8,8,3,5,7,2]))

def isPermutation(list_1, list_2):
    if len(list_2) != len(list_2):
        return False
    
    elif list_1.sort() == list_2.sort():
        return True

print(isPermutation([1,8,3,4,6],[1,4,6,8,3]))

#2D list

def sumDiagonal2D(list_data):
    total = 0

    for i in range(len(list_data)):
        total += list_data[i][i]

    return total

print(sumDiagonal2D([
    [1,8,3,4,6],
    [1,4,6,8,3],
    [1,8,3,4,6],
    [1,4,6,8,3]
]))


