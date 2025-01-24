from node import Node

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0

    def insertAtBeginning(self, city, state=None, pincode=None):
        new_node = self.createNewNode(city, state, pincode)
        if self.head is None:  # Empty list
            self.createLinkedList(new_node)
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.head = new_node
            self.tail.next = self.head  # Circular link

        self.__size += 1

    def insertAtEnd(self, city, state=None, pincode=None):
        new_node = self.createNewNode(city, state, pincode)
        if self.isEmpty():
            self.createLinkedList(new_node)
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.head.prev = new_node
            self.tail = new_node

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

        current = self.head
        while index > 0:
            current = current.next
            index -= 1
        else:
            current.prev.next = new_node
            new_node.prev = current.prev

            new_node.next = current
            current.prev = new_node

        self.__size += 1

    def deleteAtEnd(self):
        if self.isEmpty():
            print("The list is empty, nothing to delete.")
            return

        if self.head == self.tail:  # Only one node
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail

        self.__size -= 1

    def deleteAtBegin(self):
        if self.isEmpty():
            print("The list is empty, nothing to delete.")
            return

        if self.head == self.tail:  # Only one node
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head

        self.__size -= 1

    def deleteAt(self, index):
        if self.isEmpty():
            print("The list is empty, nothing to delete.")
            return

        if index == 0:
            self.deleteAtBegin()
            return

        if index >= self.__size:
            self.deleteAtEnd()
            return

        current = self.head
        while index > 0:
            current = current.next
            index -= 1
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

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

    def traversal(self):
        if self.isEmpty():
            print("The list is empty.")
            return

        current = self.head
        while True:
            print(current.city, "->", sep=" ", end=" ")
            current = current.next
            if current == self.head:
                break
        print("(head)")

        current = self.tail
        while True:
            print(current.city, "->", sep=" ", end=" ")
            current = current.prev
            if current == self.tail:
                break
        print("(tail)")

    def isEmpty(self):
        return self.head is None

    def createNewNode(self, city, state, pincode):
        return Node(city, state, pincode)

    def createLinkedList(self, new_node):
        self.head = self.tail = new_node
        self.head.next = self.head.prev = self.head
