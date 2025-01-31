from Node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.__size = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        # Create a new node
        new_node = self.createNewNode(data)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.__size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return -1

        dequeued_data = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            # Move front to the next node
            self.front = self.front.next

        self.__size -= 1

        return dequeued_data

    def get_front(self):
        if self.is_empty():
            print("Queue is empty. Cannot get front element.")
            return -1
        return self.front.data

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        current = self.front
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def createNewNode(self, data):
        return Node(data)
