number = 100
assert number > 0 ,'only positive numbers needed'
print("positive number")

def square(x):
    assert x > 0 , 'Only positive numbers needed'
    return x * x

square1 = square(20)
square_ = square(90)
print(square_)

import math

def squareRoot(number):
    assert number > 0 , " We can only take the squareroot of positive numbers"
    return math.sqrt(abs(number))

sqrt_ = squareRoot(40)
print(sqrt_)

def function(name:str, age:int) -> int:
    print(name, age)

    return name + ' ' + age

print(function('898', '34'))