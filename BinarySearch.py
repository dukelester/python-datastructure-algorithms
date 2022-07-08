#implementing a binary search

class BinarySearchNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

#inordertraversal --> leftSubtree -> root --> rightSubtree
def inOrderTraversal(root):
    if root is not None:
        #traverse left 
        inOrderTraversal(root.left)
        #traverse the root
        print(str(root.key) + "->", end="")
        #traverse right subtree
        inOrderTraversal(root.right)


#insert into a node
def insertIntoNode(node, key):
    #return a new node if the tree is empty
    if node is None:
        return BinarySearchNode(key) #creates a new node

    #traverse to the right place to insert the value
    if key < node.key:
        node.left = insertIntoNode(node.left, key)
    else:
        node.right = insertIntoNode(node.right, key)

    return node

#inorder successor
def minimumValueNode(node):
    current_node = node
    #find the left most leaf
    while current_node.left is not None:
        current_node = current_node.left
    return current_node

#deleting a node
def deleteNode(root, key):
    #if the tree is empty
    if root is None:
        return root

    #find the node to be deleted
    if key < root.key:
        root.left = deleteNode(root,left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)

    else:
        #if the node is with only one child or has no child at all
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp


        temp = minimumValueNode(root.right)
        root.key = temp.key
        
        #delete the inorder successor node
        root.right = deleteNode(root.right, temp.key)
    return root

root = None
root = insertIntoNode(root, 8)
root = insertIntoNode(root, 3)
root = insertIntoNode(root, 1)
root = insertIntoNode(root, 6)
root = insertIntoNode(root, 7)
root = insertIntoNode(root, 10)
root = insertIntoNode(root, 14)
root = insertIntoNode(root, 4)

print("Inorder traversal")
inOrderTraversal(root)
print("\n delete operation ")
root = deleteNode(root, 10)
print("Inorder traversal")
inOrderTraversal(root)

'''
The Search, insert and deletion has the best complexity of O(log n) at the best case and at the worst case
it has the O(n)

'''