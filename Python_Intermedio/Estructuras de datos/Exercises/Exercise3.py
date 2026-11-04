class Node:
    data: str

    def __init__(self,data,left=None,right=None):
        self.data = data
        self.right = right
        self.left = left 

class BinaryTree:
    root: Node

    def __init__(self,root):
        self.root = root

    def print_structure(self,current_node):
        if current_node is None:
            return
        
        print(current_node.data)

        self.print_structure(current_node.left)
        self.print_structure(current_node.right)

node6 = Node('soy node 6')
node5 = Node('soy node 5')
node4 = Node('soy node 4')
node3 = Node('soy node 3',node6)
node2  = Node('soy node 2',node4,node5)
node1 = Node('soy node 1',node2,node3)

bt = BinaryTree(node1)
bt.print_structure(bt.root)