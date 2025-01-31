from Queue import Queue

# Test the Queue
if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)

    print("Queue elements:", end=" ")
    queue.print_queue()

    print("Front element:", queue.get_front())
    queue.dequeue()

    print("Queue elements after dequeue:", end=" ")
    queue.print_queue()

    queue.enqueue(60)
    queue.print_queue()