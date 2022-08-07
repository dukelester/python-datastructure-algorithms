#a function calls itself ==> used in trees, graphs, devide and conquer, greedy algorithms and dynamic programming
''' Working with recursion:
    ==> A base condition to exit from the inifite loop of recursion
    ==> A function call 
    ==> conditional check for unintentional cases

    uses a stack memory
    fuctorial of a number n = n! ==> n * (n-1) *(n-2) * (n-3) * (n-4) ... 3 * 2 * 1
    5! = 5 * 4 * 3 * 2 * 1 ==> 120
    n! = n* (n-1)!


'''

def findFactorial(number):
    if number == 0 or number == 1: #base condition
        return 1

    if number < 0 or int(number) != number :
        return "Not defined"

    else:
        return number * findFactorial(number - 1) #recursive function call


answer = findFactorial(10)
print(answer)
#tail recursion ==> when the recursion is done at the end of the function (the last statement is recursion)

def tailRecursion(number):
    if number is None:
        return "Not defined"

    if number < 0 :
        print("the end")
        return -1
        
    else:
        print("I am tail recusrive", number)
        return tailRecursion(number - 1) #tail recursive function

result = tailRecursion(4)
print(result)

def headRecursive(number):
    if number > 0:
        headRecursive(number - 1)
        print(number)
       
    if number is None:
        return 
    
head = headRecursive(9)
print(head)

#tree recusrive function
def treeRecursive(number):
    if number == None:
        return "Unknown"
    if number > 0:
        print(number, end=" ")
        treeRecursive(number - 1)
        treeRecursive(number - 1)

        return treeRecursive(number - 1)
    else:
        return -1

result = treeRecursive(6)
print(result)

#Nested recusrive function ==> A recursive function call takes a function as a parameter
#my_func(my_func(n+1))

def nestedFunction(number):
    if number ==  None:
        return -1
    if number > 100:
        return number - 10
    else:
        return nestedFunction(nestedFunction(number + 11))

'''
    Indirect Recursion:
    In the indirect recursion, more than one function calls one another circularly.
    For example, consider three functions func_A, func_B, 
    and func_C. The func_A calls func_B, func_B calls func_C, and func_C calls func_A circularly.
'''

def function_a(number):
    if number > 0:
        print(number)
        function_b(number-1) #calling another function b

def function_b(number):
    if number > 0:
        print(number)
        function_c(number-1) #calling another function c

def function_c(number):
    if number > 0:
        print(number)
        function_a(number // 2) #calling another function a

function_a(20)



'''
Different Cases to use/avoid recursion
## Cases to use recursion

    If a problem can be broken down into similar sub-problems.
    If the time complexity and space is not an issue and,
    When we need a quick solution instead of an efficient one.
    The recursion technique can also be used with different data structure trees,
    graphs, and also with different algorithms such as the divide and conquer 
    algorithm, greedy algorithm, and dynamic programming.

## Cases to Avoid recursion

    If a problem cannot be broken down into similar sub-problems.
    If we need an efficient solution and time & space complexity are important to us.
'''








