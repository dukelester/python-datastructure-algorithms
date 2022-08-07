#Fibonacci number
'''
Fibonacci number

In this example, we use recursion to find the Fibonacci series. 
A Fibonacci series is a series of numbers in which each number is the sum of two preceding numbers. 
The sequence starts from 0 and 1. The Fibonacci sequence is given as follows.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
In the above series, consider the number 8 it is the sum of two preceding numbers 3 and 5(3 + 5 =8).

Base condition: series starts from 0 and 1  hence fib(0) = 0 and fib(1) = 1
Recursive case : fib(n ) = fib(n-1) + fib(n-2) for nth number 
Edge case .. number n must not be negative, not none , or floating point

'''

# def fibonacci(number):
#     # if number < 0 or int(number) != number:
#     #     return "Not defined"

#     if number == 0 or number == 1:
#         return number
#     else:
#         return fibonacci(number-1) + fibonacci(number - 2)

# print(fibonacci(3))

def fib(n):
    if n < 0 or int(n) != n:
        return "Not defined"
    elif n == 0 or n == 1 :
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(3))#prints Fibonacci of 4th number in series
#Output: 3

print(fib(0))#prints Fibonacci of 0th number in series
#Output: 0

print(fib(-8))#prints Fibonacci of negative number
#Output: Not defined

print(fib(1.5))#prints Fibonacci of floating-point value
#Output: Not defined


def findFib(m):
    if m == 0:
        return 1
    if m < 0 or int(m) != m:
        return "Not Defined!"

    elif m == 0 or m == 1:
        return m
    else:
        return findFib(m-1) + findFib(m -2)
