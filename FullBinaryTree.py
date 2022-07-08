# creating a full binary tree 

class FullBinaryTreeNode:
    def __init__(self,nodeData):
        self.leftChild = None
        self.rightChild = None
        self.nodeValue = nodeData

#checking for a full  binary tree
def isFullBinaryTree(rootNode):
    #check if the root node is in the full binary tree
    if rootNode is None:
        print('This is an empty binary tree')
        return True
    
    #check if the child is present
    if rootNode.leftChild is None and rootNode.rightChild is None:
        print("this tree has no child node")
        return True
    
    if rootNode.leftChild is not None and rootNode.rightChild is not None:
        return isFullBinaryTree(rootNode.leftChild) and isFullBinaryTree(rootNode.rightChild)
    return False


rootNode = FullBinaryTreeNode(1)
rootNode.leftChild = FullBinaryTreeNode(3)
rootNode.rightChild = FullBinaryTreeNode(2)

rootNode.leftChild.leftChild = FullBinaryTreeNode(4)
rootNode.leftChild.rightChild = FullBinaryTreeNode(5)
rootNode.rightChild.leftChild = FullBinaryTreeNode(9)
rootNode.rightChild.rightChild = FullBinaryTreeNode(90)

rootNode.rightChild.rightChild.rightChild = FullBinaryTreeNode(67)
rootNode.rightChild.rightChild.leftChild = FullBinaryTreeNode(80)

if isFullBinaryTree(rootNode):
    print('This is a full binary tree')
else:
    print("The binary is not a full one")

