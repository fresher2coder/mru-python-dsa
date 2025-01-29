class Stack:
    def __init__(self, capacity):
        self.stack = [0] * capacity
        self.__capacity = capacity
        self.top = -1

    def push(self, value):
        if self.isFull():
            return
        self.top +=1
        self.stack[self.top] = value

    def pop(self):
        if self.isEmpty():
            return
        top = self.stack[self.top]
        self.top -= 1
        return top

    def peek(self):
        if self.isEmpty():
            return
        return self.stack[self.top]

    def size(self):
        return self.top+1

    def isFull(self):
        return self.top+1 == self.__capacity

    def isEmpty(self):
        return self.top == -1