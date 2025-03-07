#form <file-name> import <class-name>
from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0

    def insertAtBeginning(self, city, state=None, pincode=None):

        new_node = self.createNewNode(city, state, pincode)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head ## Maintaining the cycle

        self.__size += 1

    def insertAtEnd(self, city, state=None, pincode=None):
        # new-node
        new_node = self.createNewNode(city, state, pincode)
        if self.isEmpty():
            self.createLinkedList(new_node)
        else:
            # tail->next = new-node
            # tail = new-node
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head #Maintaining the cycle

        self.__size += 1

    def insertAt(self, index, **data):
        # print(data)
        new_node = self.createNewNode(data['city'], data['state'], data['pincode'])

        if self.isEmpty():
            self.createLinkedList(new_node)
            return

        if index == 0:
            self.insertAtBeginning(data['city'], data['state'], data['pincode'])
            return

        if index >= self.__size: # 6 7 8 ....
            self.insertAtEnd(data['city'], data['state'], data['pincode'])
            return

        #traversal till the index
        prev = None
        current = self.head
        while index>0: #2 1
            prev = current
            current = current.next
            index -= 1
        else:
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
            # Traverse till the second last node
            while current.next != self.tail:
                current = current.next
            # Set tail to second last node and update its next pointer
            current.next = self.head #Maintain the cycle
            self.tail = current

        self.__size -= 1

    def deleteAtBegin(self):
        if self.isEmpty():
            print("The list is empty, nothing to delete.")
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            # Move head to the next node
            self.head = self.head.next
            self.tail.next = self.head #Maintain the cycle

        self.__size -= 1

    def deleteAt(self, index):
        if self.isEmpty():
            print("The list is empty, nothing to delete.")
            return

        if index == 0:
            self.deleteAtBegin()
            return
        #6(index: 0-5) -> index: 6, 7, 8....
        if index >= self.__size:
            self.deleteAtEnd()
            return

        prev = None
        current = self.head
        while index > 0:  # Traverse till the index
            prev = current
            current = current.next
            index -= 1
        else:
            # Remove the node
            prev.next = current.next

        self.__size -= 1

    def removeAt(self, value):
        index = self.search(value)  # Get the index of the value using search
        if index is not None:
            self.deleteAt(index)  # Use deleteAt to remove the node at the found index
        else:
            print(f"Value '{value}' not found in the list.")

    def search(self, value):
        if self.isEmpty():
            print("The list is empty.")
            return None

        current = self.head
        index = 0
        while True:
            if current.city == value:  # Match the value
                print(f"Value '{value}' found at index {index}.")
                return index
            current = current.next
            index += 1

            if current.next == self.head:
                break

        print(f"Value '{value}' not found in the list.")
        return None

    def reverse(self):
        prev = None
        current = self.head
        next_node = self.head.next

        while True:
            current.next = prev

            prev = current
            current = next_node
            next_node = next_node.next

            if next_node == self.head:
                break

        current.next = prev

        self.tail = self.head
        self.head = current
        self.tail.next = self.head #Maintain the cycle

    def traversal(self):
        current = self.head
        while True:
            print(current.city, "->", sep=" ", end=" ")
            current = current.next

            if current == self.head: #Completes the cycle
                print(current.city)
                break


    def isEmpty(self):
        return self.head is None

    def createNewNode(self, city, state, pincode):
        return Node(city, state, pincode)

    def createLinkedList(self, new_node):
        self.head = self.tail = new_node
