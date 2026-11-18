class Node:
    data:str

    def __init__(self,data,next_node=None):
        self.data = data
        self.next = next_node

class Queue:
    head: Node
    tail: Node

    def __init__(self,head=None, tail = None):
        self.head = head
        self.tail = tail

    def print_all(self):
        if self.head is None:
            print("La lista esta vacía")
            return 
        current_node = self.head

        while current_node is not None:
            if current_node is not self.head:
                print(' -> ', end='')
            print(f'{current_node.data}', end='' )
            current_node = current_node.next
        print("")

    def enqueue(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        current_node = self.tail
        self.tail = new_node
        current_node.next = self.tail

    def dequeue(self):
        if self.head == None:
            print("La lista esta vacía, no hay elementos para eliminar")
            return None
        self.head = self.head.next
        if self.head is None:
            return self.head
        return self.head.data

f = Node('F')
e = Node('E')
d = Node('D',e)
c = Node('C',d)
b = Node('B',c)
a = Node('A',b)

q = Queue()
q.enqueue("5")
q.enqueue("6")

q.enqueue("9")
q.enqueue("1")
q.print_all()
q.dequeue()
q.print_all()
q.dequeue()
q.dequeue()
q.dequeue()
q.print_all()
q.dequeue()
q.enqueue("2")
q.print_all()


