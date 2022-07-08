#create the root node

class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data
        
    #traversing inorder  :: leftSubtree -->  rootNode ---> rightSubtree
def inorderTraversal(root):
    if root:
        #traverse left
        inorderTraversal(root.left)
        #traverse root
        print(str(root.value) + "->", end="")
        #traverse the right
        inorderTraversal(root.right)

def preorderTraversal(root):
    if root: 
        #traverse the root
        print(str(root.value) + "->", end="")
        #traverse the left
        preorderTraversal(root.left)
        #traverse the right
        preorderTraversal(root.right)
      



#traversing postorder :: leftSubtree --> RightSubtree --> Rootnode
def postorderTraversal(root):
    if root: 
        #traverse the left
        postorderTraversal(root.left)
        #traverse the right
        postorderTraversal(root.right)
        #traverse the root
        print(str(root.value) + "->", end="")


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(20)

root.left.left = TreeNode(5)
root.right.right = TreeNode(7)

root.left.right = TreeNode(80)
root.left.left.right = TreeNode(100)
root.left.left.left = TreeNode(90)
print(f" \n inorder traversal is \n")
inorderTraversal(root)
print(' \nPostorder traversal\t')
postorderTraversal(root)
print(' \nPreorder traversal\t')
preorderTraversal(root)


    
