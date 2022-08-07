#stores elements linearly ++> LIFO > Last In First Out

'''
Stack Operations:
    Create A stack ==> using a list [ ]
    push =?> Ads elements to top of a stack
    pop ==> removes elemnts in LiFo procedure
    peek => retrieve the element at the top of a stack
    isEmpty => checks if the stack is empty
    isFull => checks if a stack is full
    deleteStack ==> removes all data from a stack



'''

#create a stack
class Stack:
    def __init__(self):
        self.list = []  #O(1) constant time to create a stack and space complexity is O(1)

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    #stack operations
    def isEmpty(self): #O(1) constant time to create a stack and space complexity is O(1)
        print("check if the stack is empty")
        if self.list == []:
            return True
        else:
            return False

    def pushElement(self, data_value):
        print("add an elemnt to the stack ==> push()")
        self.list.append(data_value)
        
        return "Success Insertion"

    def popItem(self):
        if self.isEmpty():
            print("Cant delete from an empty stack")
            return "Stack is empty"
        else:
            return self.list.pop() #removes the last element
    
    def peekElement(self):
        if self.isEmpty():
            print("Cant peep from an empty stack")
            return "Stack is empty"
        else:
            element = self.list[len(self.list) - 1]
            print(element)
            return element #the last element in the list 

# stack with a size
class Stack2:
    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [ str(element) for element in values]
        return '\n'.join(values)

    def pushElement(self, data_value):
        print("add an element to the stack ==> push()")
        self.list.append(data_value)
        
        return "Success Insertion"

    def isFull (self):
        if len(self.list) == self.max_size:
            return True
        else:
            return False


#create a stack using a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#creata linked list

class LinkedList:
    def __init__(self):
        self.head = None

        #iteratior function
    def __iter__(self):
        head_node = self.head
        while head_node:
            yield head_node
            head_node = head_node.next

#create a stack
class Stack3 :
    def __init__(self):
        self.LinkedList = LinkedList()

    #modify the string function
    def __str__(self):
        values = self.LinkedList
        values = [str(element.data) for element in values]
        return '\n'.join(values)


    #operations 
    def isEmpty(self):
        if self.LinkedList.head is None:
            print(True)
            return True
        else:
            return False

    #push() --> point the pointer of the head to the newly added data
    def pushValue(self, value):
        new_node = Node(value)
        if self.LinkedList.head is None:
            return "Cant do it"
        #head ==> self.LinkedList.head
        else:
            new_node.next = self.LinkedList.head
            self.LinkedList.head = new_node
            

    def pop(self):
        if self.isEmpty():
            return "Empty stack"
        else:
            temp_node = self.LinkedList.head.data
            self.LinkedList.head = self.LinkedList.head.next
            return temp_node

    def Peek(self):
        if self.isEmpty():
            return "The Stack is Empty"

        else:
            return self.LinkedList.head.data

    def delete(self): #deletes the entire stack
        self.LinkedList.head = None
        return self.LinkedList
        
        #the above operations are of oder 1 ==> O(1) for both space and time complexity



#implement 3 stacks using a single list
class MultiStack:
    def __init__(self, stackSize):
        self.numberOfSatcks = 3
        self.tempList = [0] * (stackSize * self.numberOfSatcks)
        self.sizes = [0] * self.numberOfSatcks
        self.stackSize = stackSize

    def isFull(self, numStack):
        if self.sizes[numStack] == self.stackSize:
            return True
        else:
            return False

    def isEmpty(self, numStack):
        if self.sizes[numStack] == 0:
            return True
        else:
            return False

    def topIndex(self, numStack):
        offset = numStack * self.stackSize
        return offset + self.sizes[numStack] -1

    def push(self, item, numStack):
        if self.isFull(numStack):
            return Full
        else:
            self.sizes[numStack] += 1
            self.tempList[self.topIndex(numStack)] = item

    def pop(self, numStack):
        if self.isEmpty(numStack):
            return "Empty Stack!!"
        else:
            value = self.tempList[self.topIndex(numStack)]
            self.tempList[self.topIndex(numStack)] = 0
            self.sizes[numStack] -= 1
            return value

    def peek(self, numStack):
        if self.isEmpty(numStack):
            return "Stack is Empty"
        else:
            value = self.tempList[self.topIndex(numStack)]
            return value
 

tempStack = MultiStack(6)
print(tempStack.isFull(0))
print(tempStack.isEmpty(1))
tempStack.push(100, 0)
tempStack.push(34, 2)
tempStack.push(345, 1)
tempStack.push(342, 1)
tempStack.push(45, 0)
tempStack.push(23, 2)

print(tempStack.pop(0))


open_list = [
    "[","{", "("
]
closed_list = [
    "]","}",")"
]

def checkParenthesis(myString):
    stack = []
    for  i in myString:
        if i in open_list:
            stack.append(i)
        elif i in closed_list:
            position = closed_list.index(i)
            if len(stack) > 0 and open_list[position] == stack[len(stack) - 1]:
                stack.pop()
            else:
                return "Unbalanced"

    if len(stack) ==0:
        return "Balanced"
    else:
        return "Unbalanced"




    




        



            