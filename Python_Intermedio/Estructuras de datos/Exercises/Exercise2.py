class Node:
    data:str

    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleEndedQueue:
    head: Node
    tail: Node

    def __init__(self,head,tail):
        self.head = head
        self.tail = tail

    def print_structure(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


    def push_left(self,new_node):
        current_node =  self.head
        self.head = new_node
        self.head.next = current_node
        current_node.prev = self.head


    def push_right(self,new_node):
        current_node =  self.tail
        self.tail = new_node
        self.tail.prev = current_node
        current_node.next = self.tail

    def pop_left(self):
        self.head = self.head.next
        self.head.prev = None


    def pop_right(self):
        self.tail = self.tail.prev
        self.tail.next = None

forth_node = Node("Soy el cuarto nodo")
third_node = Node("Soy el tercer nodo",forth_node)
second_node = Node("Soy el segundo nodo",third_node)
first_node = Node("Soy el primer nodo",second_node)
zero_node = Node("Soy el nodo cero")
fifth_node = Node("Soy el quinto nodo")

forth_node.prev = third_node
third_node.prev = second_node
second_node.prev = first_node


deq = DoubleEndedQueue(first_node, forth_node)
deq.print_structure()
deq.push_left(zero_node)
deq.push_right(fifth_node)
deq.print_structure()
deq.pop_left()
deq.pop_right()

deq.pop_right()

deq.pop_left()
deq.print_structure()