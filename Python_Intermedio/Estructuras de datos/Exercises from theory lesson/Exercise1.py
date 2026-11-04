class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    def enqueue(self,node):
        current_node = self.head

        if current_node == None:
            self.head = node
            return 
        while (current_node.next is not None):
            current_node = current_node.next
        current_node.next = node

    def dequeue(self):
        current_node = self.head
        if current_node.next == None:
            self.head = None
        else: 
            self.head = current_node.next


third_node = Node("Soy el tercer nodo")
second_node = Node("Soy el segundo nodo", third_node)
first_node = Node("Soy el primer nodo", second_node)
forth_node = Node("Soy el cuarto nodo")

queue = Queue(first_node)
queue.print_structure()
queue.enqueue(forth_node)
queue.print_structure()
queue.dequeue()
queue.print_structure()
queue.dequeue()
queue.print_structure()

