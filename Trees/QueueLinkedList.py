class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.headNode = None
        self.tailNode = None

    def __iter__(self):
        node = self.headNode
        while node:
            yield  node 
            node = node.next


class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = self.LinkedList
        values = [str(value) for value in values]
        return ''.join(values)

    def enqueue(self, element):
        new_node = Node(element)
        if self.LinkedList.headNode is None:
            self.LinkedList.headNode = new_node
            self.LinkedList.tailNode = new_node
        else:
            self.LinkedList.tailNode.next = new_node
            self.LinkedList.tailNode = new_node

    def isEmpty(self) :
        if self.LinkedList.headNode is None:
            return True
        else:
            return False     

    def dequeue(self):
        if self.isEmpty() :
            return "The queue is empty!!"
        else:
            temp_node = self.LinkedList.headNode
            if self.LinkedList.headNode == self.LinkedList.tailNode:
                self.LinkedList.headNode = None
                self.LinkedList.tailNode = None

            else:
                self.LinkedList.headNode = self.LinkedList.headNode.next

            return temp_node


    def delete(self):
        if self.IsEmpty():
            return "Cannot delete empty list"
        else:
            self.LinkedList.headNode = None
            self.LinkedList.tailNode = None

    def peek(self):
        if self.IsEmpty():
            return "Empty List"

        else:
            return self.LinkedList.headNode


#create a tree
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None


new_tree = TreeNode("Books")


#tree Traversal
#preorder traversal ==> Root => Left +> Right

def preorderTraversal(root_node):
    if root_node is None:
        return "empty Tree"
    
    print(root_node.data)
    preorderTraversal(root_node.left_child)
    preorderTraversal(root_node.right_child)


def inorderTraversal(root_node):
    if root_node is None:
        return
    inorderTraversal(root_node.left_child)
    print(root_node.data)
    inorderTraversal(root_node.right_child)

def postorderTraversal(root_node):
    if root_node is None:
        return "empty Tree"
    postorderTraversal(root_node.left_child)
    postorderTraversal(root_node.right_child)
    print(root_node.data)
    

#breadth first traversal ==> nodes visited level by level


def breathFisrtTraversal(root_node):
    if root_node is None:
        return -1
    else:
        visited = [root_node]

        while visited:
            current = visited.pop()
            print(current.data)
            if current.left_child is not None:
                visited.append(current.left_child)
            else :
                visited.append(root_node.right_child)


def insertaElement(root_node, new_node):
    if root_node is None:
        return -1
    else:
        visited = [root_node]

        while visited:
            current = visited.pop()
            print(current.data)
            if current.left_child is not None:
                visited.append(current.left_child)
            else:
                current.left_child = new_node
                
                return 'success'

            if current.right_child is not None:
                visited.append(root_node.right_child)
            else:
                current.right_child = new_node
                return 'success'


def insertaElement(root_node, element):
    if root_node is None:
        return -1
    else:
        visited = [root_node]

        while visited:
            current = visited.pop()
            print(current.data)
            if current.data == element:
                return 'found'

            if current.left_child is not None:
                visited.append(current.left_child)
                
            if current.right_child is not None:
                visited.append(root_node.right_child)
            

