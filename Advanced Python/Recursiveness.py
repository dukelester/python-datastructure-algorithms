#a function calling itself

def findFuctorial(x):
    if x == 1:
        return 1
    if x == 0:
        return 0
    else:
        print(x ,"*", end=' ')
        return x * findFuctorial(x-1)

answer = findFuctorial(0)
print(answer)