class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.headNode = None

     #insert at the beginning
    def insertAtBeginning(self, newNodeData):
        newNode = Node(newNodeData) #create the new node
        newNode.next = self.headNode
        self.headNode = newNode

    #insert at the end
    def insertEnd(self, newNodeData):
        newLastNode = Node(newNodeData) #create the new node
        if self.headNode is None:
            self.headNode = newNode  #create it as a new element
            return "The element at the start since no element"

        last_element = self.headNode
        while last_element.next:
            last_element = last_element.next
            last_element = newLastNode

    def insertAtMiddle(self, middleNode, newNodeData):
        if middleNode is None:
            print("abset")
            return "not found"
        newNode = Node(newNodeData)
        newNode.next = middleNode.next
        middleNode.next = newNode

    def numberOfElements(self):
        start = self.headNode
        count = 0
        while start.next != None:
            count += 1
            start = start.next
        print(count)
        return count

    def getElement(self,index):
        if index >= self.numberOfElements():
            print('index out of range')
            return None
        
        current_index = 0
        current_element = self.headNode
        while True:
            current_element = current_element.next
            if current_index == index:
                print("current element is ", current_element.data)
                return current_element.data
            current_index += 1


    def removeElement(self, elementIndex):
        if elementIndex >= self.numberOfElements():
            print("index out of range")
            return None
        current_index = 0
        current_element = self.headNode

        while True:
            last_node = current_element
            current_element = current_element.next
            if current_index == elementIndex:
                last_node.next = current_element.next
                return current_element
            current_index += 1


    def display(self):
        myElements = []
        myhead = self.headNode
        while myhead.next is not None:
            myhead = myhead.next
            myElements.append(myhead.data)
        print(myElements) 

myLinkedList = LinkedList()
myLinkedList.headNode = Node("Hello Head Node")

myLinkedList.headNode.next = Node("Next Node 1")

node2 = Node("Node 2")
node2.next = Node("node 3 next to node 3")


myLinkedList.insertAtBeginning("Lester is at the beginning")
myLinkedList.insertAtBeginning("Inserted")

myLinkedList.insertEnd("The end element")

# myLinkedList.insertAtMiddle("JUja", "Lester")
myLinkedList.display()

myLinkedList.numberOfElements()
myLinkedList.getElement(2)
myLinkedList.getElement(20)

myLinkedList.removeElement(6)
myLinkedList.removeElement(2)


myLinkedList.display()


#traverse the linked list
# use the while loop ==> traverse in forwards direction


#insertion
#at the beginning of the list




        

