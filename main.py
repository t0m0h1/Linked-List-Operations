class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def insert(self, data, index):
        if index == 0:
            self.head = Node(data, self.head)
            return

        current = self.head
        for i in range(index - 1):
            if not current:
                raise IndexError("Index out of range")
            current = current.next
        current.next = Node(data, current.next)

    def delete(self, index):
        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        for i in range(index - 1):
            if not current:
                raise IndexError("Index out of range")
            current = current.next
        current.next = current.next.next


class visualiser:
    def __init__(self):
        pass

    def visualise(self, linked_list):
        current = linked_list.head
        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("None")

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.print_list()
    linked_list.insert(4, 1)
    linked_list.print_list()
    linked_list.delete(2)
    linked_list.print_list()
    print('\n')
    print("Visualising the linked list: ")
    visualiser = visualiser()
    visualiser.visualise(linked_list)