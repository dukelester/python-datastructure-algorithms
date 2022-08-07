class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right  = None


    #insert the data
    def insert(self, data):
# Compare the new value with the parent node
      if self.data:
        # print(self.data, 'self data')
        if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
      else:
         self.data = data

    #inorder traversal ==> left --> root --> right

    def inorderTravsersal(self, root):
        elements = []
        if root:
            elements = self.inorderTravsersal(root.left)
            elements.append(root.data)

            elements = elements + self.inorderTravsersal(root.right)

        print(elements, 'in inorder traversal')
        return elements

    def postOrderTraversal(self, root):
        #left ==> right ==> root
        elements = []
        if root:
            elements = self.postOrderTraversal(root.left)  #left sub tree
            elements = elements + self.postOrderTraversal(root.right) #right sub tree
            elements.append(root.data) #add the root node
        print('post order traversal', elements)

        return elements

    def preorderTraversal(self, root):
        elements = []

        if root:
            elements.append(root.data) #start with the root
            elements = elements + self.preorderTraversal(root.left) #add the left
            elements = elements + self.preorderTraversal(root.right) #add the right

        print(elements, 'in preorderTraversal')

        return elements


    def display(self):
        # print(self.data)
        if self.left:
            self.left.display()
        if self.right:
            self.right.display()

        
    

rootNode = Node("Root")
print(rootNode.data)

rootNode.left = Node("Left Child")
rootNode.right = Node("Right Child")

print(rootNode.left.data)
print(rootNode.right.data)
        
rootNode.display()

rootNode.insert('200')
rootNode.insert('inserted')
rootNode.display()


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.inorderTravsersal(root)
root.postOrderTraversal(root)
root.preorderTraversal(root)



def findMax(data):
    max_num = 0

    for n in data:
        if n > max_num:
            max_num = n

    return max_num

result =findMax([90,78,34,50,100,99])
print(result)

def findMin(data):
    min_num = data[0]

    for n in data:
        if n < min_num:
            min_num = n 

    return min_num
result =findMin([90,78,34,50,100,99])
print(result)