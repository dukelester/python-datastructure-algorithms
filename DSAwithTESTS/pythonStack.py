#! The python Stack

'''
! Stores elements linearly. follow the LIFO ==> Last In First Out operation

! The Satck Operations::

Create a Stack =>  List is used ==> []
Push ==> insert an element into the stack ==> Insert on Top ==> insert(element, 0)
Pop ==> Removes the topmost element from the stack ==> stack.pop(0)
Peek ==> Retrieve the top element of the stack.
isEmpty => To check if the stack is empty.add()
isFull => To check if the stack is full
deletestack => to delete the elements of the stack.

'''

class Stack:
    def __init__(self):
        self.list = []
                            #! time and spoace complexity of O(1)
    def __str__(self):
        values = self.list.reverse()
        values = [str(element) for element in self.list] #! time and spoace complexity of O(n)
        return '\n'.join(values)
    
#!Operations in a Stack
    #is empty()
    def isEmpty(self):   #! time and spoace complexity of O(1)
        if len (self.list) == 0:
            return True
        else:
            return False
        
    def push(self, element):
        self.list.append(element)
        return f'{element} was successfully inserted into the stack'

    def pop(self):
        if self.isEmpty():
            return 'The stack is empty and we can not remove any element'
        else:
            removed = self.list.pop()
            print(f'{removed}...removing an element now ****')
            return removed
        
    def peek(self):
        if self.isEmpty():
            return 'The stack is empty and we can not get peek element'
        else:
            # return self.list[len(self.list) - 1]
                return self.list[-1]
            
    def delete(self):
        self.list = None
        
    
        
temp_stack = Stack()
print(temp_stack.isEmpty())
temp_stack.push(39)
temp_stack.push(34)
temp_stack.push(36)
print(temp_stack.push(78))
print(temp_stack.isEmpty())

temp_stack.pop()
print(' ')
print(temp_stack.peek(), 'peek')
# temp_stack.delete()
print(temp_stack)

#create a stack with a size of elements

class MyStack:
    def __init__(self, length):
        self.length = length
        self.list = [ ] #initializes an empty list

    #string representation of the stack
    def __str__(self):
        values_of_stack = self.list.reverse()
        values = [ str(value) for value in self.list]
        return '\n'.join(values)

    #check if the stack is empty ie ==> length == 0
    def isEmpty(self):
        return self.length == 0

    #check if its full ==> len(list) == length
    def isFull(self):
        if len(self.list)  == self.length:
            return True
        else:
            return False

    #add an element into the stack:
    def Push(self, element):
        #check if the stack is full 
        if self.isFull():
            return "We can not Add a new element .... stack is full!"
        else:
            self.list.append(element)
            return f'{element} was added successfully'

    #remove an element from the stack...
    def Pop(self):
        #check if the stack is empty...
        if self.isEmpty():
            return 'The stack is empty !!'
        else:
            self.list.reverse()
            self.list.pop()
            return f'removed {self.list.pop()} '

    def Peek(self):
        if self.isEmpty():
            return 'Empty Stack !!'
        else:
            return self.list[-1] #the last element ==> last in element is the peek element 

my_stack = MyStack(20)
print(my_stack.isEmpty())
print(my_stack.isFull())
my_stack.Push(78)
my_stack.Push(70)
my_stack.Push(73)
print(my_stack.Push(74))

print(my_stack.Pop())
my_stack.Push(48)
my_stack.Push(00)
print(my_stack)

print(my_stack.Peek(), 'peek element')

#! create a stack from a linked list::
'''
A linked list is made up of nodes ==> each node has data and a pointer to the next node.
a linked list is a type of a list so it can be used to create a stack.
the 1rst element in a linked list is a Head and the last element is a Tail.. whose pointer 
points tpo null
Nodes are created via classes;
*** using linked list will make the operations such as traversal, insertion, deletion, search faster tahn
a normal list ***
'''

class Node:
    def __init__(self, data):
        self.data = data #the data for the linked list
        self.next = None #the next pointer

#create a linked list and start at the head:
class LinkedList:
    def __init__(self):
        self.head = None

    #format the printing of the elements of a linked list by overiding the __iter__() method::
    def __iter__(self):
        node = self.head #get the head node as the first element
        while node: #while the head is not None
            yield node #return the node and continue
            node = node.next #update the node ( current head node ) to the next node ==> node.next
    
#create a stack

class LinkedListStack:
    def __init__(self):
        self.linkedList = LinkedList() #creating alinked list

    #the string representation of the linked list elements
    def __str__(self):
        linked_values = self.linkedList
        values = [ str(value.data) for value in self.linkedList ] #using the list comprehension to get each element
        return ' ==> '.join(values)

    #Operations on Stack using Linked List
    #! 1. isEmpty() => the stack is empty if the head node points to none
    def isEmpty(self):
        if self.linkedList.head is None:
            return True
        else:
            return False

    #push() ==> add elements into a linked list --> the head pointer points to the new node created
    def PushToStack(self, value):
        new_node = Node(value) #create a node
        new_node.next = self.linkedList.head #new node's pointer points to the head
        self.linkedList.head = new_node #the new node becomes the head

    #POP() => we remove the topmost element in the stack ==> which is the head in our case
    def PopFromStack(self):
        if self.isEmpty():
            return 'We can not remove from an empty Stack'
        else:
            current_node = self.linkedList.head.data #to be returned
            print('We poped this out  ==> ', current_node)
            self.linkedList.head = self.linkedList.head.next #we assign the next element from the node to the node itself
            return current_node #the poped item

    def GetThePeek(self):
        #the peek element is the top most element which is the head
        if self.isEmpty():
            return 'We dont have a Peek element'
        else:
            return self.linkedList.head.data

    def deleteStack(self):
        if self.isEmpty():
            return "already empty"
        else:
            self.linkedList.head = None

'''
 Opeartion         Time Complexity      SpaceComplexity

Create Stack        O(1)                    O(1)
Push                O(1)                    O(1)
Pop                 O(1)                    O(1)
Peek                O(1)                    O(1)
isEmpty             O(1)                    O(1)
Delete Entire Stack O(1)                    O(1)

'''


print('\n\n ****************Linked List Stack****************\n')
linked_list_stack = LinkedListStack()
print(linked_list_stack.isEmpty())
linked_list_stack.PushToStack(89)
linked_list_stack.PushToStack(90)
linked_list_stack.PushToStack(57)
linked_list_stack.PushToStack(70)
linked_list_stack.PushToStack(50)
linked_list_stack.PushToStack(67)
linked_list_stack.PushToStack(40)
print(linked_list_stack)
linked_list_stack.PopFromStack()
print(linked_list_stack)
print('I am the peek element', linked_list_stack.GetThePeek())
print(linked_list_stack.deleteStack())



#check if the parenthesis are valid or not:
opening_brackets = [ '(', '[', '{']
closing_brackets = [ ')', ']', '}']
stack = []
def checkBrackets(my_bracket_string):
    for i in my_bracket_string:
        if i in opening_brackets:
            stack.append(i)
        elif i in closing_brackets:
            position = closing_brackets.index(i)
            if len(stack) > 0 and opening_brackets[position] == stack[len(stack) - 1]:
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return 'Balanced'
    else:
        return "Unbalanced"


brackets = "[ {}}{{]]()(((())))"
brackets_2 = " [ { ( } )]"
print(checkBrackets(brackets))
print(checkBrackets(brackets_2))





