def reverseString(str):
    reversed_str = ""
    for i in str:
        reversed_str = i + reversed_str
    print(reversed_str)
    
    
reverseString("duke")

reverseString("hello duke lester here I am")

#using the while loop

def reverse2(word):
    my_reversed = ""
    count = len(word)
    while count > 0:
        my_reversed = my_reversed + word[count - 1]
        count -= 1
        
    print(my_reversed)
    
reverse2("here is my string")

#using the slice operators

def myString(str):
    str = str[::-1]
    print(str)
    
myString("Hello")

#using reversed and join

def usingReversed(str):
    newString = "".join(reversed(str))
    
    print(newString)
    
usingReversed("lester")
    
    
#recusrion

def reverseRecursion(str):
    if len(str) == 0:
        return str
    else:
        return reverseRecursion(str[1:]) + str[0]
        
        
result = reverseRecursion("here is a nother recursion")
print(result)


numbers = [4, 2, 6, 7, 3, 5, 8, 10, 6, 1, 9, 2]  

squares = [x **2 for x in numbers]

set_squares = set(squares)


print(squares, set_squares)


for n in numbers:
    if n %2 !=0:
        print(n)
else:
    print('not inside the loop')
for number in numbers:
    if all(number % i !=0 for i in range(2,number)):
        print(number)

tuple_ = ("Python", "Loops", "Sequence", "Condition", "Range")  
upper_ = []
for name in range(0, len(tuple_)):
    print(tuple_[name].upper())
    upper_.append(tuple_[name].upper())
print(upper_)

