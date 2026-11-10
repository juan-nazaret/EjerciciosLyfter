class Node:
    data: int

    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    head: Node

    def __init__(self,head):
        self.head = head


    def print_all(self):
        print('\n')
        current_node = self.head

        while current_node is not None:
            if current_node is not self.head:
                print(' -> ', end='')
            print(current_node.data,end='')
            current_node = current_node.next
        

    def insert_front(self,data):
        current_node = self.head
        self.head = data 
        self.head.next = current_node


    def insert_back(self,data):
        current_node = self.head
        if current_node is None:
            self.head = data
            return 
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next =  data


    def delete(self,data):
        current_node = self.head
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
linked_list = LinkedList(A)
linked_list.insert_front(B)

linked_list.insert_back(C)
linked_list.print_all()
linked_list.delete(20)
linked_list.delete(10)
linked_list.delete(30)
linked_list.insert_back(B)
linked_list.print_all()