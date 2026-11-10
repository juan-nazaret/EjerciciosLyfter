class Node:
    data:str

    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Queue:
    head: Node

    def __init__(self,head):
        self.head = head

    def print_all(self):
        current_node = self.head

        while current_node is not None:
            if current_node is not self.head:
                print(' -> ', end='')
            print(f'{current_node.data}', end='' )
            current_node = current_node.next

    def enqueue(self,new_node):
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node


    def dequeue(self):
        self.head = self.head.next
        return self.head

f = Node('F')
e = Node('E')
d = Node('D',e)
c = Node('C',d)
b = Node('B',c)
a = Node('A',b)

queue = Queue(a)
queue.print_all()
queue.enqueue(f)
queue.print_all()
queue.dequeue()
queue.print_all()
