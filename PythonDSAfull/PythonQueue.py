#the queue => FIFO

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
        

    def enqueue(self, item):
        self.items.append(item)

        return "Success"

    def dequeue(self):
        if self.isEmpty():
            return "empty"
        else:
            return self.items.pop(0) 

    def peek(self):
        if self.isEmpty():
            return "Empty"
        else:
            return self.items[0]

    def delete(self):
        self.items = None


#create a queue using a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next


class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = self.LinkedList
        values = [ str(element) for element in values]
        return ''.join(values)

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def enqueue(self, element):
        new_node = Node(element)
        if self.LinkedList.head is None:
            self.LinkedList.head = new_node
            self.LinkedList.tail = new_node
        else:
            self.LinkedList.tail.next = new_node
            self.LinkedList.tail = new_node

    def dequeue(self):
        if self.isEmpty():
            return "The Queue is empty"
        else:
            current_node = self.LinkedList.head
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head = self.LinkedList.head.next
            return current_node

    def peek(self):
        if self.isEmpty():
            return "No Head"
        else:
            return self.LinkedList.head

        
    def delete(self):
        self.LinkedList.head = None
        return 'deleted'




#circular queue
class CircularQueue:
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.items = maxSize * [None]
        self.front = -1
        self.rear = -1

    def isFull(self):
        if self.rear + 1 == self.front + 1:
            return True
        elif self.front == 0 and self.rear + 1 == self.maxSize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else: return False
        
    
    def enqueue(self, value):
        if self.isFull():
            return "Cannot add"

        else:
            if self.rear + 1 == self.maxSize:
                self.rear = 0
            else:
                self.rear +=1 
                if self.front == -1:
                    self.front =0

            self.items[self.rear] = value

            return "success"

    #dequeue Function to insert elements 
    def dequeue(self):
        if self.isEmpty():
            return "The circular queue is empty."
        else:
            firstElement = self.items[self.front]
            front = self.front
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            elif self.front + 1 == self.maxSize:
                self.front = 0
            else:
                self.front += 1
            self.items[front] = None
            return firstElement

            #peek Function to return the topmost element
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.items[self.front]

    #delete Function to the entire queue.
    def delete(self):
        self.items = self.maxSize * [None]
        self.rear = -1
        self.front = -1


        '''
        Time and Space Complexity for Operations on Circular Queue

        Time Complexity	SpaceComplexity
        Create Queue	O(1)	O(n)
        Enqueue	O(1)	O(1)
        Dequeue	O(1)	O(1)
        Peek	O(1)	O(1)
        isEmpty/isFull	O(1)	O(1)
        Delete Entire Queue	O(1)	O(1)
        '''


#Implementing queue using two stacks
class Stack():
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if len(self.list) == 0:
            return None
        return self.list.pop()


class QueueviaStack():
    def __init__(self):
        self.in_Stack = Stack()
        self.out_Stack = Stack()

    def enqueue(self, item):
        self.in_Stack.push(item)

    def dequeue(self):
        while len(self.in_Stack):
            self.out_Stack.push(self.in_Stack.pop())
        result = self.out_Stack.pop()
        while len(self.out_Stack):
            self.in_Stack.push(self.out_Stack.pop())
        return result


    
'''
An animal shelter operating strictly on “First-In/First-Out” basis holds only dogs and cats. 
People can select either a dog or a cat (and will recieve the oldest animal, based on arrival,
 of that type) or can take the oldest animal. Design a data structure to maintain this system,
 which includes functions such as enqueue, dequeueAny, dequeueDog, and dequeueCat.
'''

class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self,animal, type):
        if type == 'Cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeueAny(self):
        if len(self.dogs) == 0:
            result = self.cats.pop(0)
            return result

        else:
            result = self.dogs.pop(0)
            return result


    def dequeueCat(self):
        if len(self.cats) == 0:
            return "Empty cats"
        else:
            return self.cats.pop(0)

    def dequeueDog(self):
        if len(self.dogs) == 0:
            return "Empty Dogs"
        else:
            return self.dogs.pop(0)




import queue

list_ = queue.Queue(maxsize=30)
list_.put('Duke klester')
list_.put('Jello')
list_.put('Duke ')
list_.put('Dug')

print(list_.get())
print(list_.get())
print(list_.get())
print(list_.get())
print(list_.get())