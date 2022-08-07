class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def __iter__(self):
        current  = self.head
        while current:
            yield  current
            current = current.next
            print(current)

    def insertBeginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
        print('inserted ', data)

    def insertBetween(self, data, middle_node):
        new_node = Node(data)
        if middle_node is None:
            return "Node not found"
        else:
            new_node.next = middle_node.next
            middle_node.next = new_node

    def insertAtEnd(self, data):
        new_end_node = Node(data)
        if self.head is None:
            self.head = new_end_node
            self.tail = new_end_node
            return 
        else:
            current_node = self.head
            while current_node.next: #O(N) ==> insertaion at the end
                current_node = current_node.next
            current_node.next = new_end_node
            self.tail = new_end_node

    
   
    #traversing
    def printList(self):
        current_node = self.head
        while current_node:#O(N) ==> traversing time complexity
            print(current_node.data)
            current_node = current_node.next

    def searchForElement(self, element):
        position = 0

        if self.head is None:
            return "empty list"
        elif self.head.data == element:
            return self.head.data

        else:
            current = self.head
            while current:
                position += 1
                if current.data == element:
                    print('found at position' , position)
                    return True
                current = current.next

    def deleteAtBeginning(self):
        if self.head is None:
            return "Empty List"
        elif self.head.next == self.tail.next:
            self.head = self.tail = None
            return "Deleted the Head node"

        elif self.head is not None:
            temp_node = self.head
            self.head = self.head.next
            temp_node = None
            return "Done deleting the first element"


    #Function to delete a node from between the linked list
    def delMid(self, del_value):
            temp_head = self.head
            if (temp_head is not None):
                if (temp_head.value == del_value):
                    self.head = temp_head.next
                    temp_head = None
                    return

            while (temp_head is not None):
                if temp_head.value == del_value:
                    break
                prev = temp_head
                temp_head = temp_head.next

            if (temp_head == None):
                return

            prev.next = temp_head.next
            temp_head = None

        #Function to delete node from the end
    def delEnd(self):
            if(self.head == None):
                return
            elif (self.head.next == self.tail.next):
                self.head = self.tail = None
                return
            else:
                temp_node = self.head
                while (temp_node.next is not self.tail):
                    temp_node = temp_node.next
                self.tail = temp_node
                temp_node.next = None
            return

    def deleteEntireList(self):
        if self.head:
            self.head = None
            self.tail = None
        else:
            return "Empty List already"

myLinkedList = SinglyLinkedList()
head_node = Node('Head Node')
head_node.next = Node("Next Node")
myLinkedList.head = head_node
myLinkedList.head.next = head_node.next 
myLinkedList.tail = Node("Tail")
myLinkedList.insertAtEnd(809)
myLinkedList.insertAtEnd(34)
myLinkedList.insertBeginning(56)
myLinkedList.printList()
myLinkedList.searchForElement(34)
myLinkedList.deleteAtBeginning()

myLinkedList.printList()