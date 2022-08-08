class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insertIntoBinarySearchTree(root_node, new_node_value):
    if root_node.data is None:
        root_node.data = new_node_value
        return BinarySearchTree(new_node_value)

    else:
        if new_node_value < root_node.data:
            if root_node.left_child is None:
                root_node.left_child = BinarySearchTree(new_node_value)
            else:
                insertIntoBinarySearchTree(root_node.left_child, new_node_value)

        else:
            if new_node_value > root_node.data:
                if root_node.right_child is None:
                    root_node.right_child = BinarySearchTree(new_node_value)
                else:
                    insertIntoBinarySearchTree(root_node.right_child, new_node_value)

    return "Success"



def preorderTraversal(root_node):
    if root_node  is None:
        return "Empty Tree"

    else:
        print(root_node.data) 
        preorderTraversal(root_node.left_child)
        preorderTraversal(root_node.right_child)
    
def postorderTraversal(root_node):
    if root_node  is None:
        return "Empty Tree"
    else:
        postorderTraversal(root_node.left_child)
        postorderTraversal(root_node.right_child)
        print(root_node.data)

def inorderTraversal(root_node):
    if root_node  is None:
        return "Empty Tree"

    else:
        inorderTraversal(root_node.left_child)
        print(root_node.data)
        inorderTraversal(root_node.right_child)


def breadthFirstTraversal(root_node):
    if root_node is None:
        return "Empty Tree"
    visited = [ root_node ]

    while visited:
        current_node = visited.pop()
        print(current_node.data)

        if current_node.left_child is not None:
            visited.append(current_node.left_child)
        if current_node.right_child is not None:
            visited.append(current_node.right_child)



def searchForElement(root_node, element):
    if root_node is None:
        return "Empty Tree"
    if root_node.data == element:
        return f"found {root_node.data}"

    else:
        if element < root_node.data:
            if root_node.left_child is not None and root_node.left_child.data  == element:
                return "found"
            else:
                searchForElement(root_node.left_child, element)
            

        else:
            if element > root_node.data:
                if root_node.right_child is not None and root_node.right_child.data == element:
                    return "found"
                else:
                    searchForElement(root_node.right_child, element)

                




new_binary_tree = BinarySearchTree(None)
insertIntoBinarySearchTree(new_binary_tree,34)
print(new_binary_tree.data)

print(insertIntoBinarySearchTree(new_binary_tree, 90))
print(insertIntoBinarySearchTree(new_binary_tree, 3))
print(insertIntoBinarySearchTree(new_binary_tree, 45))
print(insertIntoBinarySearchTree(new_binary_tree, 12))
print(insertIntoBinarySearchTree(new_binary_tree, 78))

preorderTraversal(new_binary_tree)
postorderTraversal(new_binary_tree)
inorderTraversal(new_binary_tree)
breadthFirstTraversal(new_binary_tree)

print(searchForElement(new_binary_tree, 90))
print(searchForElement(new_binary_tree, 902))
print(searchForElement(new_binary_tree, 2))
