
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
            print(f'{current_node.data}')
            current_node = current_node.next

    def push(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        current_node = self.head
        self.head = Node(data)
        self.head.next = current_node

    def pop(self):
        current_node = self.head
        if self.head == None:
            print('La lista esta vacía')
        else:
            self.head = self.head.next
        return current_node

    def sort(self):
        if self.head == None:
            print("No hay elementos para ordenar")
        elif self.head.next is None:
            return print(self.head.data)
        else: 
            #obtains the length of the stack
            number_of_interactions = self.count_items()
            self.bubble_sort(number_of_interactions)


    def count_items(self):
        current_node = self.head
        counter = 0
        while current_node is not None:
            counter += 1
            current_node = current_node.next
        return counter 


    def bubble_sort(self,number_of_items):
        aux: Node
    
        for outer_index in range(number_of_items- 1):
            current_node = self.head
            next_node = current_node.next
            for index in range(0,(number_of_items-1)-outer_index):
                if current_node.data > next_node.data:
                    if current_node is self.head:
                        self.head = next_node
                        current_node.next = self.head.next
                        self.head.next = current_node
                        current_node = self.head.next
                        next_node = current_node.next
                        aux = self.head
                        current_node = self.head.next
                        next_node = current_node.next
                        continue
                    aux.next = next_node
                    current_node.next = next_node.next
                    next_node.next = current_node
                    aux = next_node
                    next_node = current_node.next
                else:
                    aux = current_node
                    current_node = next_node
                    next_node = current_node.next
                    
        
q = Stack()
q.push(2)
q.push(1)
q.push(6)
q.push(9)
q.print_structure()
q.sort()
print('ordenada:')
q.print_structure()
q.push(15)
q.sort()
print('ordenada:')
q.print_structure()

