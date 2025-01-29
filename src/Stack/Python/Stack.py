class Stack:
    def __init__(self):
        self.stack = []
        self.__size = 0

    def push(self, value):
        self.stack.append(value)
        self.__size += 1

    def pop(self):
        if self.isEmpty():
            return None
        self.__size -= 1
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

    def isEmpty(self):
        return self.__size == 0

    def size(self):
        return self.__size