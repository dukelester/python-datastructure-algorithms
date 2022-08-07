#using recursion to find a factorial of a number
import sys

sys.setrecursionlimit(200)
print(sys.getrecursionlimit())
def findFactorial(number):
    if number == 0:
        return 1
    return number * findFactorial(number - 1)


answer = findFactorial(10)
print(answer)