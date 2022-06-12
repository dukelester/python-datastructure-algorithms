"""
Basic Operations of Queue
A queue is an object (an abstract data structure - ADT) that allows the following operations:

Enqueue: Add an element to the end of the queue
Dequeue: Remove an element from the front of the queue
IsEmpty: Check if the queue is empty
IsFull: Check if the queue is full
Peek: Get the value of the front of the queue without removing it
Working of Queue
Queue operations work as follows:

two pointers FRONT and REAR
FRONT track the first element of the queue
REAR track the last element of the queue
initially, set value of FRONT and REAR to -1
Enqueue Operation
check if the queue is full
for the first element, set the value of FRONT to 0
increase the REAR index by 1
add the new element in the position pointed to by REAR
Dequeue Operation
check if the queue is empty
return the value pointed by FRONT
increase the FRONT index by 1
for the last element, reset the values of FRONT and REAR to -1
"""

class Queue:
    def __init__(self):
        self.queue = []
        
    #add an element
    def enqueue(self, item):
        self.queue.append(item)
        
    #remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    #display the queue
    def display(self):
        print(self.queue)
    #find the size of the queue
    def size(self):
        return len(self.queue)
    
Q = Queue()
print(Q.size(), 'size of the queue')
Q.enqueue(89)
Q.enqueue(90)
Q.enqueue(69)
Q.enqueue(99)
Q.enqueue(29)
Q.display()

Q.dequeue()
Q.display()
