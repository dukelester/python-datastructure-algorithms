#the balanced binary tree

class BalancedTreeNode:
    def __init__(self, nodeData):
        self.leftChild = None
        self.rightChild = None
        self.rootNode = nodeData

    
class Height:
    def __init__(self):
        self.height = 0

def isHeightBalanced(rootNode,height):
    left_height = Height()
    right_height = Height()

    if rootNode is None:
        return True

    left = isHeightBalanced(rootNode.leftChild, left_height)
    right = isHeightBalanced(rootNode.rightChild, right_height)
    height.height = max(left_height.height, right_height.height) + 1

    if abs(left_height.height - right_height.height) <= 1:
        return left and right
    return False


height = Height()
rootNode = BalancedTreeNode(1)
rootNode.leftChild = BalancedTreeNode(2)
rootNode.rightChild =BalancedTreeNode (3)
rootNode.leftChild.leftChild = BalancedTreeNode (4)
rootNode.leftChild.rightChild = BalancedTreeNode(5)

if isHeightBalanced(rootNode, height):
    print('This is a balanced binary tree')
else:
    print('This is not a balanced binary tree')