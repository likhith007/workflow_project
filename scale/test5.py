class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def remove_node(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
        else:
            current = self.head
            previous = None
            while current is not None and current.value != value:
                previous = current
                current = current.next

            if current is not None:
                previous.next = current.next

    def search_value(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def get_length(self):
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next
        return length

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
