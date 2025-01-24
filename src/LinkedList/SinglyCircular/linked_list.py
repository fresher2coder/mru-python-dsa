from node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0

    def insertAtBeginning(self, city, state=None, pincode=None):
        new_node = self.createNewNode(city, state, pincode)
        if self.isEmpty():  # Empty list
            self.createLinkedList(new_node)
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head  # Maintain circular link

        self.__size += 1

    def insertAtEnd(self, city, state=None, pincode=None):
        new_node = self.createNewNode(city, state, pincode)
        if self.isEmpty():
            self.createLinkedList(new_node)
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head  # Maintain circular link

        self.__size += 1

    def insertAt(self, index, **data):
        new_node = self.createNewNode(data['city'], data['state'], data['pincode'])

        if self.isEmpty():
            self.createLinkedList(new_node)
            return

        if index == 0:
            self.insertAtBeginning(data['city'], data['state'], data['pincode'])
            return

        if index >= self.__size:  # Out of bounds, insert at the end
            self.insertAtEnd(data['city'], data['state'], data['pincode'])
            return

        # Traverse till the index
        prev = None
        current = self.head
        while index > 0:
            prev = current
            current = current.next
            index -= 1

        prev.next = new_node
        new_node.next = current

        self.__size += 1

    def deleteAtEnd(self):
        if self.isEmpty():
            print("The list is empty, nothing to delete.")
            return

        if self.head == self.tail:  # Only one node
            self.head = self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = self.head  # Maintain circular link
            self.tail = current

        self.__size -= 1

    def deleteAtBegin(self):
        if self.isEmpty():
            print("The list is empty, nothing to delete.")
            return

        if self.head == self.tail:  # Only one node
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head  # Maintain circular link

        self.__size -= 1

    def deleteAt(self, index):
        if self.isEmpty():
            print("The list is empty, nothing to delete.")
            return

        if index == 0:
            self.deleteAtBegin()
            return

        if index >= self.__size:  # Out of bounds, delete at the end
            self.deleteAtEnd()
            return

        prev = None
        current = self.head
        while index > 0:
            prev = current
            current = current.next
            index -= 1

        prev.next = current.next

        self.__size -= 1

    def removeAt(self, value):
        index = self.search(value)
        if index is not None:
            self.deleteAt(index)
        else:
            print(f"Value '{value}' not found in the list.")

    def search(self, value):
        if self.isEmpty():
            print("The list is empty.")
            return None

        current = self.head
        index = 0
        while True:
            if current.city == value:
                print(f"Value '{value}' found at index {index}.")
                return index
            current = current.next
            index += 1
            if current == self.head:  # Completed one full cycle
                break

        print(f"Value '{value}' not found in the list.")
        return None

    def reverse(self):
        prev = None
        current = self.head
        next_node = None

        if self.isEmpty():
            return

        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

            if current == self.head:  # Completed one full cycle
                break

        self.tail = self.head
        self.tail.next = prev
        self.head = prev

    def traversal(self):
        if self.isEmpty():
            print("The list is empty.")
            return

        current = self.head
        while True:
            print(current.city, "->", sep=" ", end=" ")
            current = current.next
            if current == self.head:  # Completed one full cycle
                break
        print("(head)")

    def isEmpty(self):
        return self.head is None

    def createNewNode(self, city, state, pincode):
        return Node(city, state, pincode)

    def createLinkedList(self, new_node):
        self.head = self.tail = new_node
        self.tail.next = self.head  # Circular link


