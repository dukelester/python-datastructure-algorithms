#Binary tree implementation


#create the node
class BinaryTreeNode:
    def __init__(self, nodeData):
        self.left = None
        self.right = None
        self.value = nodeData

    #traversing the binary tree preorderTraversal
    def traverseBinaryPreOrder(self):
        print(str(self.value) + " ->", end="")
        if self.left:
            self.left.traverseBinaryPreOrder()
        if self.right:
            self.right.traverseBinaryPreOrder()
        
    #traverse the binary tree inorderTraversal
    def traverseBinaryInOrder(self):
        if self.left:
            self.left.traverseBinaryInOrder()
        print(str(self.value) + "->", end="")
        if self.right:
            self.right.traverseBinaryInOrder()
    
    #traverse the binary tree postoder
    def traverseBinaryPostOrder(self):
        if self.left:
            self.left.traverseBinaryPostOrder()
        if self.right:
            self.right.traverseBinaryPostOrder()
        print(str(self.value) + "->", end="")


rootNode = BinaryTreeNode(67)
rootNode.left = BinaryTreeNode(30)
rootNode.right = BinaryTreeNode(20)

#add other children
rootNode.left.left = BinaryTreeNode(50)
rootNode.left.right = BinaryTreeNode(20)

print('Traverse in Inorder \n')
rootNode.traverseBinaryInOrder()
print('Travserse in postorder \n')
rootNode.traverseBinaryPostOrder()
print('Traverse in pre order \n')
rootNode.traverseBinaryPreOrder()