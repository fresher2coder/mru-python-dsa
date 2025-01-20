from Node import Node


class LinkedList:
    """Linked list implementation."""
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, city):
        """Insert a node at the end of the linked list."""
        new_node = Node(city)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_beginning(self, city):
        """Insert a node at the beginning of the linked list."""
        new_node = Node(city)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at(self, city, pos):
        """Insert a node at a specific position in the linked list."""
        new_node = Node(city)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            current = self.head
            prev = None
            while current is not None and pos > 1:
                prev = current
                current = current.next
                pos -= 1

            if current is None:
                self.insert_at_end(city)
            elif current == self.head:
                self.insert_at_beginning(city)
            else:
                prev.next = new_node
                new_node.next = current

    def delete_at_end(self):
        """Delete a node from the end of the linked list."""
        if self.head is None:
            print("List is Empty")
        else:
            current = self.head
            prev = None
            while current != self.tail:
                prev = current
                current = current.next

            if current == self.head:
                self.head = self.tail = None
            else:
                prev.next = None
                self.tail = prev

    def delete_at_beginning(self):
        """Delete a node from the beginning of the linked list."""
        if self.head is None:
            print("List is Empty")
        else:
            current = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None

    def delete_at(self, city):
        """Delete a node with a specific value."""
        if self.head is None:
            print("List is Empty")
        elif self.head.city == city:
            self.delete_at_beginning()
        elif self.tail.city == city:
            self.delete_at_end()
        else:
            current = self.head
            prev = None
            while current is not None and current.city != city:
                prev = current
                current = current.next

            if current is None:
                print(f"{city} is not found")
            else:
                prev.next = current.next

    def search(self, city):
        """Search for a city in the linked list."""
        current = self.head
        while current:
            if current.city == city:
                return True
            current = current.next
        return False

    def traversal(self):
        """Traverse and display the linked list."""
        current = self.head
        if self.head is None:
            print("List is empty")
            return

        while current:
            print(f"{current.city} -> ", end="")
            current = current.next
        print("None")


