# creating a perfect binary tree 

class PerfectBinaryTreeNode:
    def __init__(self,nodeData):
        self.leftChild = None
        self.rightChild = None
        self.nodeValue = nodeData

#calculate the depth
def calculateDepth(treeNode):
    depth = 0
    while treeNode is not None:
        depth += 1
        treeNode = treeNode.leftChild
    return depth


#check if the tree is a perfect binary tree
def isPerfectTree(rootNode, depth, level = 0):
    #check if the tree is empty
    if rootNode is None:
        return True
    #check for trees
    if rootNode.leftChild is None and rootNode.rightChild is None:
        return depth == level + 1

    if rootNode.leftChild is None or rootNode.rightChild is None:
        return False #not a perfect tree
    return isPerfectTree(rootNode.leftChild, depth, level + 1) and isPerfectTree(rootNode.rightChild, depth, level + 1)


rootNode = None
rootNode = PerfectBinaryTreeNode(1)
rootNode.leftChild = PerfectBinaryTreeNode(2)
rootNode.rightChild = PerfectBinaryTreeNode(3)

rootNode.leftChild.leftChild = PerfectBinaryTreeNode(4)
rootNode.leftChild.rightChild = PerfectBinaryTreeNode(5)

if isPerfectTree(rootNode, calculateDepth(rootNode)):
    print("This is a perfect binary tree")
else:
    print('This is not a perfect binary tree')


