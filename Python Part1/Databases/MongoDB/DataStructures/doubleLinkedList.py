class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self, head):
        self.head = head

    def addElement(self, newData):
        newNode = Node(newData)
        newNode.next = self.head

        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode

    # Define the insert method to insert the element		
    def insert(self, prev_node, NewVal):
        if prev_node is None:
            return
        NewNode = Node(NewVal)
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        NewNode.prev = prev_node
        if NewNode.next is not None:
            NewNode.next.prev = NewNode



    def display(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next



node1 = Node("node1")
node2 = Node("node2")
node3 = Node("node3")
node4 = Node("node4")
node5 = Node("node5")

double_linked_list = DoubleLinkedList(node1)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = node5

double_linked_list.addElement("Hello")

double_linked_list.display()


