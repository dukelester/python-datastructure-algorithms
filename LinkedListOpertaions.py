from html.entities import html5
from more_itertools import iterate


class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertBeginning(self, item):
        #create a node 
        node = Node(item, self.head)
        self.head = node
        
    def insertEnd(self,item):
        if self.head is None:
            self.head = Node(item, None)    
            return
        iterate =self.head
        while iterate.next:
            iterate = iterate.next
        iterate.next = Node(item, None)
        return
    
    def insertValues(self, data_list):
        self.head = None
        for data in data_list:
            self.insertEnd(data)
            
    def getLengthOfList(self):
        count = 0
        iterate = self.head
        while iterate:
            count +=1
            iterate = iterate.next
            
        return count
        
        
    def removeElementAtPosition(self, position):
        if position < 0 or position > self.getLengthOfList():
            raise Exception('Invalid position')
        
        if position == 0:
            self.head = self.head.next
            return 
        count = 0
        iterate = self.head
        while iterate:
            if count == position - 1:
                iterate.next = iterate.next.next
                break
            iterate = iterate.next
            count += 1
        
    def display(self):
        if self.head is None:
            print('empty linked list')
            return 
        iterate = self.head
        
        result = ''
        while iterate:
            result += str(iterate.item) + '----> '
            
            iterate = iterate.next
        print(result)
        
        
        
if __name__ == '__main__':
    linkedlist =  LinkedList()
    linkedlist.insertBeginning(89)
    linkedlist.insertBeginning(49)
    linkedlist.insertBeginning(79)
    linkedlist.insertBeginning(99)
    linkedlist.display()
    linkedlist.insertEnd(100)
    linkedlist.insertEnd(670)
    linkedlist.display()
    linkedlist.insertValues([1,2,3,4,5,6,7,8,9,10])
    linkedlist.display()
    print(linkedlist.getLengthOfList(), 'length of the list')
    linkedlist.removeElementAtPosition(2)
   
    linkedlist.display()
    
        
