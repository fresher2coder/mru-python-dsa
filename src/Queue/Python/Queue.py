class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)  # Adds to the end (O(1))

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.pop(0)  # Removes from the front (O(n))

    def front(self):
        if self.is_empty():
            return None
        return self.queue[0]  # Returns front element (O(1))

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)  # O(1)

    def print_queue(self):
        print(self.queue)


