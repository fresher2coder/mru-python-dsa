from Queue import Queue

if __name__ == "__main__":

    # Usage Example
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print(q.dequeue())  # Output: 10
    print(q.front())    # Output: 20
    print(q.size())     # Output: 2
    print(q.is_empty()) # Output: False