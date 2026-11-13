class Node:
    data: str

    def __init__(self,data,next =None):
        self.data = data
        self.next = next

class Stack:
    head: Node

    def __init__(self, head=None):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push(self,new_node):
        current_node = self.head
        self.head = new_node
        self.head.next = current_node

    def pop(self):
        current_node = self.head
        if self.head == None:
            print('La lista esta vacía')
        else:
            self.head = self.head.next
        return current_node


first_node = Node("Soy el primer nodo")
second_node = Node("Soy el segundo nodo")
third_node = Node("Soy el tercer nodo")
forth_node = Node("Soy el cuarto nodo")
fifth_node = Node('soy el quinto nodo')
sixth_node = Node('Soy el sexto nodo')
stack = Stack(forth_node)
#stack.print_structure()
stack.push(fifth_node)
stack.print_structure()
print('*****')
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.push(sixth_node)

stack.print_structure()


print('bye')