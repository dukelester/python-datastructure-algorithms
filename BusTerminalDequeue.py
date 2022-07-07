class BusTerminalDequeue:
    def __init__(self):
        self.bus_queue = [] #initialize the dequeue
    #add to the queue
    def addBusOnFront(self, bus):
        self.bus_queue.insert(0, bus)
        return f" added the {bus} at the front "
    
    def addBusOnEnd(self, bus):
        self.bus_queue.append(bus)
        return f" added the {bus} at the end of the queue"

    def removeBusFromEnd(self):
        if len(self.bus_queue) > 1:
            self.bus_queue.pop()
            return f" Removed the bus at the end of the queue"
        else:
            return "the queue is empty"
    
    def removeBusFromFront(self):
        if len(self.bus_queue) > 1:
            self.bus_queue.pop(0) 
            return f" Removed the bus at the front of the queue"
        else:
            return f"The queue is empty"
    
    def displayDequeue(self):
        return self.bus_queue


terminal_queue = BusTerminalDequeue()
print(terminal_queue.displayDequeue())
terminal_queue.addBusOnFront("Super Metro")
terminal_queue.addBusOnFront("Trans Metro")
terminal_queue.addBusOnFront("Kenny Sacco")
terminal_queue.addBusOnFront("Afya Trans")
print(terminal_queue.displayDequeue())

terminal_queue.addBusOnEnd("KBS")
terminal_queue.addBusOnEnd("Mattis")
terminal_queue.addBusOnEnd("Lopha travellers")

print(terminal_queue.displayDequeue())
terminal_queue.removeBusFromEnd()
print(terminal_queue.displayDequeue())

terminal_queue.removeBusFromFront()

print(terminal_queue.displayDequeue())

