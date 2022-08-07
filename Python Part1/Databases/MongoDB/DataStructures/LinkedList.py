class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        while self.head is not None:
            print(self.head)
            self.head = self.head.next
        
linked_list = LinkedList()
linked_list.head = Node("hello")
linked_list.next = Node("lester")

linked_list.display()




