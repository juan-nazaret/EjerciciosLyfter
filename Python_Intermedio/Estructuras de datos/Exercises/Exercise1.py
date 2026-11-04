class Node:
    data: str

    def __init__(self,data,next =None):
        self.data = data
        self.next = next

class Stack:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push(self,new_node):
        self.head = new_node

    def pop(self):
        if self.head.next == None:
            self.head = None
        else:
            self.head = self.head.next


first_node = Node("Soy el primer nodo")
second_node = Node("Soy el segundo nodo",first_node)
third_node = Node("Soy el tercer nodo",second_node)
forth_node = Node("Soy el cuarto nodo", third_node)

stack = Stack(third_node)
stack.print_structure()
print("\npush*****")
stack.push(forth_node)
stack.print_structure()
print("\npop******")
stack.pop()
stack.pop()
stack.pop()

stack.print_structure()
