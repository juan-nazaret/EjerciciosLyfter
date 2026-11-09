class Node:
    data:str

    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleEndedQueue:
    head: Node
    tail: Node

    def __init__(self,head=None,tail=None):
        self.head = head
        self.tail = tail

    def print_structure(self):
        if self.head == None:
            print('la lista esta vacía')
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


    def push_left(self,new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        
        else:
            current_node =  self.head
            self.head = new_node
            self.head.next = current_node
            current_node.prev = self.head


    def push_right(self,new_node):
        if self.tail == None:
            self.tail = new_node
            self.head = new_node
        else:
            current_node =  self.tail
            self.tail = new_node
            self.tail.prev = current_node
            current_node.next = self.tail

    def pop_left(self):
        current_node = self.head
        if self.head == None:
            print('no hay elementos para eliminar, la lista esta vacía')
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            current_node.next = None
            current_node.prev = None        
        return current_node

    def pop_right(self):
        current_node = self.head
        if self.tail == None:
            print('no hay elementos para eliminar, la lista esta vacía')
        elif self.tail is self.head:
            self.tail = None
            self.head = None
        else:
            current_node = self.tail
            self.tail = self.tail.prev
            current_node.next = None
            current_node.prev = None
        return current_node

forth_node = Node("Soy el cuarto nodo")
third_node = Node("Soy el tercer nodo")
second_node = Node("Soy el segundo nodo")
first_node = Node("Soy el primer nodo")
zero_node = Node("Soy el nodo cero")
fifth_node = Node("Soy el quinto nodo")

forth_node.prev = third_node
third_node.prev = second_node
second_node.prev = first_node


deq = DoubleEndedQueue()

deq.print_structure()

deq.pop_left()
deq.pop_right()

print('****')
deq.print_structure()


deq.pop_left()
print('****')
deq.print_structure()


deq.pop_right()
print('****')

deq.pop_right()
deq.pop_right()

deq.pop_right()

deq.pop_right()
deq.pop_left()
deq.pop_left()
deq.pop_left()
deq.pop_left()

deq.push_right(second_node)
print('///////')
deq.print_structure()
print('888888')
deq.push_left(third_node)
deq.print_structure()

deq.print_structure()
print(f'{deq.tail.data} and {deq.head.data}')