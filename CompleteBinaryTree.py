#a complete binary tree

class CompleteBinaryTreeNode:
    def __init__(self, nodeData):
        self.leftChild = None
        self.rightChild = None
        self.treeNode = nodeData

#count the numbe of nodes;
def countNodes(rootNode):
    if rootNode is None:
        return 0
    return 1 + countNodes(rootNode.leftChild) + countNodes(rootNode.rightChild)

#check if the tree is a complete binary tree
def checkCompleteBinaryTree(rootNode, index, numberOfNodes):
    #check if empty
    if rootNode is None:
        return True
    if index >= numberOfNodes:
        return False
    return (
        checkCompleteBinaryTree(rootNode.leftChild, 2 * index, numberOfNodes) 
    and 
    checkCompleteBinaryTree(rootNode.rightChild, 2*index,numberOfNodes)
    )

rootNode = CompleteBinaryTreeNode(1)
rootNode.leftChild = CompleteBinaryTreeNode(2)
rootNode.rightChild = CompleteBinaryTreeNode(3)

rootNode.leftChild.leftChild = CompleteBinaryTreeNode(4)
rootNode.leftChild.rightChild = CompleteBinaryTreeNode(5)

node_count = countNodes(rootNode)
index = 0
if checkCompleteBinaryTree(rootNode, index,node_count):
    print("This is a complete binary tree")
else:
    print('This is not a complete binary tree')

