'''
    Consider a number num = 3214. The sum of digits in the number num is (3 + 2 + 1 + 4 = 10).
        Now, to obtain each digit separately, we perform the modular and division operation.

        The (num % 10) gives the last digit, and the statement (num // 10) 
        removes the last digit and returns the remaining part of the number. 
        The function is then called recursively for the remaining digits.


        In the following code, we declare a user-defined function sum_digits() 
        that takes a number num as a parameter.

        Base Condition: The smallest possible input for the recursive function 
        sum_digits is 0. Hence, the recursion process stops when the number is reduced to 0.
        Recursive case: We call the function recursively for the remaining part 
        of the number, excluding the last digit. The recursive call is 
        sum_digits(num) = (num%10) + sum_digits(n//10).
        Unintentional cases: The number num should not be a negative number 
        or a floating-point value. Otherwise, the program returns the unexpected output.


'''

# print((3214 % 10) + (3214 // 10))
# print(3214 // 10)

def findSum(number):
    if number == 0:
        return -1

    elif number < 0 or int(number) != number:
        return "Undefined"
    else:
        return (number % 10) + findSum(number // 10)

print(findSum(98765))



def findPower(number, exponent):
    if number < 0 or int(number) != number:
        return "Only Positive whole numbers needed !"
    elif exponent == 0:
        return 1
    elif  int(exponent) != exponent:
        return "Undefined" 

    else:
        return number * findPower(number, exponent - 1)

print(findPower(2, 9))

