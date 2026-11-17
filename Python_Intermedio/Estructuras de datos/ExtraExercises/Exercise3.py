class Node:
    data: str

    def __init__(self,data,next_node=None, prev = None):
        self.data = data
        self.next = next_node
        self.prev = prev

class DoublyLinkedList:
    head: Node
    tail: Node
    def __init__(self,head=None, tail=None):
        self.head = head
        self.tail = tail

    def print_forward(self):
        if self.head is None:
            print("La lista esta vacía")
            return 
        current_node = self.head
        while current_node is not None:
            if current_node is not self.head:
                print(' -> ',end='')
            print(current_node.data,end='')
            current_node = current_node.next
        print("")


    def print_backward(self):
        if self.head is None:
            print("La lista esta vacía")
            return
        current_node = self.tail
        while current_node is not None:
            if current_node is not self.tail:
                print(' -> ',end='')
            print(current_node.data, end='')
            current_node = current_node.prev
        print("")

    def append(self,data):
        new_node = Node(data)
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
            return
        current_node = self.tail
        self.tail = Node(data)
        self.tail.prev = current_node
        current_node.next = self.tail


    def prepend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        current_node = self.head
        self.head =  Node(data)
        self.head.next = current_node
        current_node.prev = self.head


    def delete(self,data):
        current_node = self.head
        if current_node.data == data:
            self.head = current_node.next
            current_node.next = None
            if self.head is None:
                self.tail = None
                return current_node
            self.head.prev = None
            current_node.next = None
            return current_node  #retorna el nodo eliminado
        while current_node.next is not None:
            next_node = current_node.next
            if next_node.data == data:
                current_node.next = next_node.next
                if current_node.next is not None:
                    current_node.next.prev = current_node
                else:
                    self.tail = current_node
                next_node.next = None
                next_node.prev = None
                
                return current_node #retorna el nodo eliminado
            current_node = current_node.next




deq = DoublyLinkedList()
deq.append("E")
deq.prepend("0")
deq.prepend("89")
deq.append("7")
deq.prepend("0")

deq.print_forward()
deq.print_backward()

deq.delete("89")
deq.print_backward()
deq.print_forward()
deq.delete("0")
deq.print_backward()
deq.print_forward()

deq.delete("7")
deq.print_backward()
deq.prepend("ESO")
deq.print_forward()