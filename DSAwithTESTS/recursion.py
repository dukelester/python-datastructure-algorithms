#recursion in python
'''
here a function makes a call to itself
breaks a problem into a smaller simpler problem for ease solving
used in ==> Trees, graphs, devide and conquer functions, dynamic programming, greedy algorithms.


Working of recursion:
Find a base condition =>  to exit from an infinite loop.
function call => a function calls itself with smaller inputs.
condition for the unintentional cases ==> to avaoid edge cases and check if the input is valid.

uses a stack memory to store the function calls.==> O(n) and O(n) for the space and time complecity.

'''


def factorialOfNumber(number):
    #check for edge cases
    if number < 0 or int(number) != number:
        return "undefined"
    if number == 0 or number == 1: #base condition
        return 1
    else:
        return number * factorialOfNumber(number - 1) #recursive call
    
def fibonacciOfNumber(number):
     #check for edge cases
    if number < 0 or int(number) != number:
        return "undefined"
    
    if number == 0 or number == 1: #base condition
        return number
    
    else:
        return fibonacciOfNumber(number -1 ) + fibonacciOfNumber(number-2)
    

'''
Types of recursion:
1. Direct recursion( tail, head, nested, tree)  => The function calls itself unti a base condition is met
2. Indirect Recursion


(i) Tail Recursion ++> recursive call is the last statement in the function body. Operations are perfomed during function call

'''

#!Tail Recursion
def tailRecursive(radius):
    if radius == 0:
        return 0
    else:
        print(radius * radius * 3.14)
        return tailRecursive(radius-1)
    
# tailRecursive(5)

#! head Recursion  => the recursive call is the first statement in the function body

def headRecursive(radius):
    if radius > 0:
        headRecursive((radius - 1))
        print(radius * radius * 3.14)
        
    elif radius == 0:
        return 0
    
# headRecursive(5)

print(3234//10,  3234%10)


def sumOfDigitsOfNumber(num):
    if num  < 0 or int(num) != num:
        return "undefined"
    if num == 0:
        return 0
    
    else:
        return (num % 10) + sumOfDigitsOfNumber(num // 10)
    
print(sumOfDigitsOfNumber(56789033))

def findPower(num, power):
    if num  < 0 or int(num) != num:
            return "undefined"
    if num == 0:
        return 0
    if power < 0 or int(power) != power:
        return "not defined"
    if power == 0:
        return 1
    else:
        return num * findPower(num, power - 1)
    
print(findPower(2, 3))

def findGCD(num1, num2):
    if num1 < 0 :
        num1 = -num1
    if num2 < 0:
        num2 = -num2
    if int(num1) != num1 or int(num2) != num2:  #avoid float numbers
        return "They Must be integers"
    
    if num2 == 0: #!base condition
        return num1
    else:
        return findGCD(num1, (num1 % num2))

def decimalToBinary(n):
    if int(n) != n :
        return "Only Integers please!"
    if n == 0:
        return 0
    else:
        return ( n % 2)  + 10 * (decimalToBinary(int(n / 2)))

print(decimalToBinary(67))



def reverseList(list1, i, j):
    if i < j:
        temp = list1[i]
        list1[i] = list1[j]
        list1[j] = temp
        reverseList(list1, i+1, j-1)
        
    print(list1)

my_list = [1,2,3,4,5]
reverseList(my_list,0, len(my_list) - 1)

def isPrimeNumber(number, n):
    if n is None:
        n = number -1
    while n > 2:
        if number % n == 0:
            return "Not Prime"
        else:
            return isPrimeNumber(number, n-1)
    else:
        return "Prime Number"


def decimalToBinary2(number):
    if number > 1:
        decimalToBinary2(number // 2)
    print(number % 2, end="")

decimalToBinary2(950)

def getLargest(list_):
    if len(list_) == 1:
        return list_[0]
    else:
        m = getLargest(list_[1:])
        return m if m > list_[0] else list_[0]
print()
def reverseString(string):
    if len(string) == 0:
        return string
    else:
        return reverseString(string[1:]) + string[0]


print(reverseString(" \n duke lester"))

print(isPrimeNumber(89, 2))
print(isPrimeNumber(88, 4))