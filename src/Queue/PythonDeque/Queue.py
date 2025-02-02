from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()  # Initialize an empty deque

    def enqueue(self, item):
        """Adds an item to the end of the queue (O(1) operation)."""
        self.queue.append(item)

    def dequeue(self):
        """Removes and returns the front item from the queue (O(1) operation)."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.popleft()

    def front(self):
        """Returns the front item of the queue without removing it."""
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Returns the number of elements in the queue."""
        return len(self.queue)


