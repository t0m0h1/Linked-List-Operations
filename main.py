class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    class LinkedList:
        def __init__(self):
            # Initialize an empty linked list with no head node
            self.head = None

        def append(self, data):
            # If the linked list is empty, create a new node and set it as the head
            if not self.head:
                self.head = Node(data)

            current = self.head
            # Traverse to the last node
            while current.next:
                current = current.next
            # Create a new node and set it as the next node of the last node
            current.next = Node(data)
        

        def print_list(self):
            current = self.head
            # singly linked lists start with the head node
            while current:
                print(current.data)
                current = current.next


        def insert(self, data, index):
            # If the index is 0, insert the new node at the head
            if index == 0:
                self.head = Node(data, self.head)
                return

            current = self.head
            # Traverse to the node before the index
            for i in range(index - 1):
                if not current:
                    raise IndexError("Index out of range")
                current = current.next
            # Create a new node and set it as the next node of the current node
            current.next = Node(data, current.next)


        def delete(self, index):
            # If the index is 0, delete the head node
            if index == 0:
                self.head = self.head.next
                return

            current = self.head
            # Traverse to the node before the index
            for i in range(index - 1):
                if not current:
                    raise IndexError("Index out of range")
                current = current.next
            # Set the next node of the current node to the next node of the next node
            current.next = current.next.next