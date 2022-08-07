#memoization to find the fibonacci of a number

def findFibonacci(num, memory):
    if num == 1:
        return 0
    if num == 2:
        return 1
    if not num in memory:
        memory[num] = findFibonacci(num-1, memory) + findFibonacci(num -2, memory)
        return memory[num]

# print(findFibonacci(9,{} ))

def numberFactor(number, tempDict):
    if number < 0:
        return -1
    if number in (0, 1 ,2):
        return 1
    elif number == 3:
        return 2

    else:
        subpart1 = numberFactor(number-1, tempDict)
        subpart2 = numberFactor(number-3, tempDict)
        subpart3 = numberFactor(number-4, tempDict)

        tempDict[number] = subpart1 + subpart2 + subpart3
        return tempDict[number]

print(numberFactor(5, {}))
print(numberFactor(1, {}))
print(numberFactor(0, {}))
print(numberFactor(3, {}))