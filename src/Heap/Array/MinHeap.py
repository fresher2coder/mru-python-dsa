class MinHeap:
    def __init__(self, capacity=100):
        self.heap = []
        self.capacity = capacity

    # Get parent, left, and right child index
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
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    # Extract min (delete root)
    def delete(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last element to root
        self._heapify_down(0)  # Heapify down from root
        return root

    # Heapify Down (for deletion)
    def _heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    # Heap Sort
    def heapsort(self):
        sorted_array = []
        while self.heap:
            sorted_array.append(self.delete())
        return sorted_array

    # Get Min
    def get_min(self):
        return self.heap[0] if self.heap else None

    # Print Heap
    def print_heap(self):
        print(self.heap)


# Example Usage
min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(4)
min_heap.insert(15)
min_heap.insert(7)
min_heap.insert(3)

print("Min Heap:")
min_heap.print_heap()

print("Deleted Min:", min_heap.delete())

print("Heap after deletion:")
min_heap.print_heap()

print("Heap Sort Result:", min_heap.heapsort())
