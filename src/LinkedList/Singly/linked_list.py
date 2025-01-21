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

    def traversal(self):
        current = self.head
        while current is not None:
            print(current.city, "->", sep=" ", end=" ")
            current = current.next
        else:
            print("None")

    def isEmpty(self):
        return self.head is None

    def createNewNode(self, city, state, pincode):
        return Node(city, state, pincode)

    def createLinkedList(self, new_node):
        self.head = self.tail = new_node
