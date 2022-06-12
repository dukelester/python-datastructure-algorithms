'''
Stack Data Structure
 stack is a linear data structure that follows the principle of Last In First Out (LIFO). This means the last element inserted inside the stack is removed first.

You can think of the stack data structure as the pile of plates on top of another.

elements on stack are added on top and removed from top just like a pile of plate
Stack representation similar to a pile of plate
Here, you can:

Put a new plate on top
Remove the top plate
And, if you want the plate at the bottom, you must first remove all the plates on top. This is exactly how the stack data structure works.

LIFO Principle of Stack
In programming terms, putting an item on top of the stack is called push and removing an item is called pop.

represent the LIFO principle by using push and pop operation
Stack Push and Pop Operations
In the above image, although item 3 was kept last, it was removed first. This is exactly how the LIFO (Last In First Out) Principle works.

We can implement a stack in any programming language like C, C++, Java, Python or C#, but the specification is pretty much the same.

Basic Operations of Stack

There are some basic operations that allow us to perform different actions on a stack.

Push: Add an element to the top of a stack
Pop: Remove an element from the top of a stack
IsEmpty: Check if the stack is empty
IsFull: Check if the stack is full
Peek: Get the value of the top element without removing it
Working of Stack Data Structure
The operations work as follows:

A pointer called TOP is used to keep track of the top element in the stack.
When initializing the stack, we set its value to -1 so that we can check if the stack is empty by comparing TOP == -1.
On pushing an element, we increase the value of TOP and place the new element in the position pointed to by TOP.
On popping an element, we return the element pointed to by TOP and reduce its value.
Before pushing, we check if the stack is already full
Before popping, we check if the stack is already empty

'''

#implementation in python 

def createStack():
    stack = []  #empty    
    return stack

#check if empty
def checkEmpty(stack):
    if len(stack) == 0:
        return True
    else:
        return False
    
#adding items to the stack use push

def addItems(stack, item):
    stack.append(item) #adding item to the stack
    print('pushed an item ', item , 'to the stack')
    return stack

def removeElement(stack):
    if checkEmpty(stack):
        return 'the stack is empty'
    else:
        return stack.pop()
        
    
    
    
my_stack = createStack()
print(my_stack, 'my stack')
is_empty = checkEmpty(my_stack)
print(is_empty, 'my stack is empty')
add_number = addItems(my_stack, 500)
print(add_number, 'added to the stack')
remove_element = removeElement(my_stack)
print(remove_element)
# for k in range(0,4):
#     remove_element = removeElement(my_stack)
#     print(remove_element)

#the push and pop functions take only constant time 0(1)

class MysStack(object):
    def __init__(self):
        self.my_stack = []
    
    def push(self, item):
        item = self.my_stack.append(item)
        return item
    
stacky = MysStack()
stacky.push(900)

print(stacky.my_stack)
print(stacky.top())