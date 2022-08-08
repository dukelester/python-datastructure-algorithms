"""

To create a basic tree in python, we first initialize the 
“TreeNode” class with the data items and a list called “children”. 
Then, we will edit the “__str__” function to print the node values as 
if they were a tree. Lastly, we’ll create a function to add nodes to the tree
"""


class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def addChild(self, TreeNode):
        self.children.append(TreeNode)


tree = TreeNode("Marks", [])
math = TreeNode('Mathematics', [])
eng = TreeNode("English", [])

tree.addChild(math)
tree.addChild(eng)

print(tree)

