class Dequeue:
    
    def __init__(self):
        self.myQueue = []
        
    #check if empty
    def isEmpty(self):
        if len(self.myQueue) == 0:
            return True
        else:
            return False
    #insert at the end
    def addRear(self, item):
        self.myQueue.append(item)
        return item
    #add to the front
    def addFront(self, item):
        self.myQueue.insert(0, item)
        return item
    #remove the last element
    def removeRear(self):
        return self.myQueue.pop()
    def removeFisrt(self):
        return self.myQueue.pop(0)
    
    #size of the queue
    def size(self):
        return len(self.myQueue)
    
    #display the queue
    def display(self):
        print(self.myQueue)
    
my_queue = Dequeue()
my_queue.display()
my_queue.addRear(455)
my_queue.addRear(855)
my_queue.addRear(405)
my_queue.display()
my_queue.addFront(90)
my_queue.addFront(10)
my_queue.addFront(80)
my_queue.display()

my_queue.removeFisrt()
my_queue.display()
my_queue.removeRear()
my_queue.display()