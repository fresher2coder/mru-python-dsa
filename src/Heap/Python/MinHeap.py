import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    # Insertion into MinHeap
    def insert(self, val):
        heapq.heappush(self.heap, val)

    # Deletion from MinHeap (removes the smallest element)
    def delete(self):
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            return None

    # Heapsort
    def heapsort(self):
        sorted_list = []
        while self.heap:
            sorted_list.append(self.delete())
        return sorted_list

    def get_min(self):
        if self.heap:
            return self.heap[0]
        else:
            return None

    def print_heap(self):
        print(self.heap)

# Example Usage
min_heap = MinHeap()
min_heap.insert(3)
min_heap.insert(1)
min_heap.insert(2)
min_heap.insert(6)
min_heap.insert(5)
min_heap.insert(9)


print("Min Heap:")
min_heap.print_heap()

print("Deleted min:", min_heap.delete())

print("Min Heap after deletion:")
min_heap.print_heap()

print("Sorted Heap using Heapsort:")
print(min_heap.heapsort())
