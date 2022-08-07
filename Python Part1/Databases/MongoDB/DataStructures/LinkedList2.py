#create a node
class Node:
    def __init__(self, data= None):
        self.data = data
        self.next_pointer = None
        

#create the linked list
class LinkedList:
    def __init__(self):
        self.head = None #the first element in the linked list

    def insertAtBeginning(self, new_node_data):
        newNode = Node(new_node_data)
        #change the pointer
        self.head = newNode
        self.head.next_pointer = newNode


    def displayData(self):
        mydata = self.head
        while mydata is  not None:
            print(mydata.data)
            mydata =  mydata.next_pointer


#create a list object
myLinkedList = LinkedList()

myLinkedList.insertAtBeginning("duke")
#create nodes
node1 = Node("Monday")
node2 = Node("Tuesday")
node3 = Node("Wednesday")
myLinkedList.head = Node("Sunday")


#point the head to the next element
myLinkedList.head.next_pointer = node1
node1.next_pointer = node2
node2.next_pointer = node3

myLinkedList.displayData()

