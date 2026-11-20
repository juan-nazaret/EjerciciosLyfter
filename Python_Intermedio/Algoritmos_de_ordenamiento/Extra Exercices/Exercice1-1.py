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


    def sort(self):
        if self.head == None:
            print("No hay elementos para ordenar")
        elif self.head.next is None:
            return print(self.head.data)
        else: 
            #obtains the length of the stack
            number_of_interactions = self.count_items()
            self.bubble_sort(number_of_interactions)
            print('Lista ordenada\n')


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
                        current_node.prev = self.head
                        self.head.prev = None
                        self.head.next = current_node
                        current_node = self.head.next
                        next_node = current_node.next
                        aux = self.head
                        current_node = self.head.next
                        next_node = current_node.next
                        continue
                    if next_node is self.tail:
                        aux.next = next_node
                        next_node.next = current_node
                        next_node.prev = aux
                        current_node.prev = next_node
                        current_node.next = None
                        self.tail = current_node
                        aux = next_node
                        next_node = None
                        continue
                    aux.next = next_node
                    current_node.next = next_node.next
                    current_node.prev = next_node
                    next_node.next = current_node
                    next_node.prev = aux
                    if current_node.next is not None:
                        current_node.next.prev = current_node
                    aux = next_node
                    next_node = current_node.next
                else:
                    aux = current_node
                    current_node = next_node
                    next_node = current_node.next


deq = DoublyLinkedList()
deq.append(9)
deq.prepend(0)
deq.prepend(8)
deq.append(7)
deq.prepend(3)


deq.sort()
deq.print_forward()
deq.print_backward()

deq.append(1)
deq.print_forward()
deq.print_backward()
deq.sort()

deq.print_forward()
deq.print_backward()
deq.delete(8)
deq.sort()

deq.print_forward()
deq.print_backward()
deq.prepend(10)
deq.print_forward()
deq.print_backward()
deq.sort()

deq.print_forward()
deq.print_backward()
