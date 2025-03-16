class MaxHeap:
    def __init__(self, capacity=100):
        self.heap = []
        self.capacity = capacity

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    # Insert element into heap
    def insert(self, val):
        if len(self.heap) >= self.capacity:
            print("Heap is full")
            return

        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    # Heapify Up (for insertion)
    def _heapify_up(self, index):
        while index > 0 and self.heap[index] > self.heap[self.parent(index)]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    # Extract max (delete root)
    def delete(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    # Heapify Down (for deletion)
    def _heapify_down(self, index):
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    # Heap Sort
    def heapsort(self):
        sorted_array = []
        while self.heap:
            sorted_array.append(self.delete())
        return sorted_array

    # Get Max
    def get_max(self):
        return self.heap[0] if self.heap else None

    # Print Heap
    def print_heap(self):
        print(self.heap)


# Example Usage
max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(4)
max_heap.insert(15)
max_heap.insert(7)
max_heap.insert(3)

print("Max Heap:")
max_heap.print_heap()

print("Deleted Max:", max_heap.delete())

print("Heap after deletion:")
max_heap.print_heap()

print("Heap Sort Result:", max_heap.heapsort())
