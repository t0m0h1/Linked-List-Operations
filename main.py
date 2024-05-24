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
        