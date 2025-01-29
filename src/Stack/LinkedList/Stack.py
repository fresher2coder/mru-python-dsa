from Node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.__size = 0

    def push(self, value):
        new_node = self.createNode(value)

        if self.isEmpty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.__size += 1

    def pop(self):
        if self.isEmpty():
            return
        top = self.top.value
        self.top = self.top.next
        self.__size -= 1
        return top

    def peek(self):
        if self.isEmpty():
            return
        return self.top.value

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.top == None
    def createNode(self, value):
        return Node(value)
