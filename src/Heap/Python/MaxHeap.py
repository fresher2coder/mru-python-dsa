import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    # Insertion into MaxHeap
    def insert(self, val):
        self.heap.append(val)
        heapq.heappush(self.heap, -val)

    # Deletion from MaxHeap (removes the largest element)
    def delete(self):
        if self.heap:
            return -heapq.heappop(self.heap)
        else:
            return None

    # Heapsort
    def heapsort(self):
        sorted_list = []
        while self.heap:
            sorted_list.append(self.delete())
        return sorted_list

    def get_max(self):
        if self.heap:
            return -self.heap[0]
        else:
            return None

    def print_heap(self):
        print([-x for x in self.heap])

# Example Usage
max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(1)
max_heap.insert(6)
max_heap.insert(5)
max_heap.insert(9)
max_heap.insert(2)

print("Max Heap:")
max_heap.print_heap()

print("Deleted max:", max_heap.delete())

print("Max Heap after deletion:")
max_heap.print_heap()

print("Sorted Heap using Heapsort:")
print(max_heap.heapsort())
