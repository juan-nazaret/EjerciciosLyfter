class Node:
    data: int

    def __init__(self,data,next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    head: Node

    def __init__(self,head=None):
        self.head = head


    def print_all(self):
        current_node = self.head
        if current_node is None:
            print("Nada que imprimir, la lista esta vacía", end="")
        while current_node is not None:
            if current_node is not self.head:
                print(' -> ', end='')
            print(current_node.data,end='')
            current_node = current_node.next
        print("")

    def insert_front(self,data):
        current_node = self.head
        #the new Node will be the new head
        self.head = Node(data)
        self.head.next = current_node


    def insert_back(self,data):
        current_node = self.head
        if current_node is None:
            self.head = Node(data)
            return 
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next =  Node(data)


    def delete(self,data):
        current_node = self.head
        if current_node is None:
            print("La lista ya esta vacía")
            return 
        if current_node.data == data:
            self.head = self.head.next
            current_node.next = None
            return
        while current_node is not None and current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            else:
                current_node = current_node.next
            


C = Node(30)
B= Node(20)
A = Node(10)
ll = LinkedList()
ll.insert_front(20)
ll.insert_back(30)
ll.print_all()
ll.insert_back(50)
ll.print_all()
ll.delete(30)
ll.print_all()
ll.delete(50)
ll.delete(20)
ll.print_all()
ll.delete(50)