class Queue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.queue = [None] * self.__capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1 and self.rear == -1

    def is_full(self):
        return (self.rear + 1) % self.__capacity == self.front

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return

        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.__capacity

        self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return
        front = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.__capacity

        return front

    def get_front(self):
        if self.is_empty():
            print("Queue is empty. Cannot get front element.")
            return None
        return self.queue[self.front]

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.__capacity
        print()



