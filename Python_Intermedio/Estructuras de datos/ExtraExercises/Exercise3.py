class Node:
    data: str

    def __init__(self,data,next=None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class Deque:
    head: Node
    tail: Node
    def __init__(self,head, tail):
        self.head = head
        self.tail = tail

    def print_forward(self):
        print('\n')
        current_node = self.head
        while current_node is not None:
            if current_node is not self.head:
                print(' -> ',end='')
            print(current_node.data,end='')
            current_node = current_node.next


    def print_backward(self):
        print('\n')
        current_node = self.tail
        while current_node is not None:
            if current_node is not self.tail:
                print(' -> ',end='')
            print(current_node.data, end='')
            current_node = current_node.prev


    def append(self,data):
        current_node = self.tail
        self.tail = data
        self.tail.prev = current_node
        current_node.next = self.tail


    def prepend(self,data):
        current_node = self.head
        self.head =  data
        self.head.next = current_node
        current_node.prev = self.head


    def delete(self,data):
        current_node = self.head
        if current_node.data == data:
            self.head = current_node.next
            self.head.prev = None
            current_node.next = None
            return
        while current_node.next is not None:
            next_node = current_node.next
            if next_node.data == data:
                print(next_node.next)
                current_node.next = next_node.next
                try:
                    current_node.next.prev = current_node
                except AttributeError as ex:
                    self.tail = current_node
                next_node.next = None
                next_node.prev = None
                
                return
            current_node = current_node.next

forth_node = Node("D")
third_node = Node("C",forth_node)
second_node = Node("B",third_node)
first_node = Node("A",second_node)
zero_node = Node("0")
fifth_node = Node("E")

forth_node.prev = third_node
third_node.prev = second_node
second_node.prev = first_node


deq = Deque(first_node, forth_node)
deq.prepend(zero_node)
deq.append(fifth_node)

deq.delete("E")
deq.print_forward()
deq.print_backward()

