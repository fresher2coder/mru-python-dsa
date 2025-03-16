class MaxHeap:
    def __init__(self):
        self.root = None
        self.nodes = []

    def insert(self, key):
        new_node = Node(key)
        if not self.root:
            self.root = new_node
        else:
            parent = self.nodes[(len(self.nodes) - 1) // 2]
            if not parent.left:
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent
            self._heapify_up(new_node)
        self.nodes.append(new_node)

    # Heapify Up (for insertion)
    def _heapify_up(self, node):
        while node.parent and node.key > node.parent.key:
            node.key, node.parent.key = node.parent.key, node.key
            node = node.parent

    # Extract max (delete root)
    def delete(self):
        if not self.root:
            return None
        if len(self.nodes) == 1:
            max_val = self.root.key
            self.root = None
            self.nodes.pop()
            return max_val

        max_val = self.root.key
        last_node = self.nodes.pop()
        if last_node.parent:
            if last_node.parent.right == last_node:
                last_node.parent.right = None
            else:
                last_node.parent.left = None

        self.root.key = last_node.key
        self._heapify_down(self.root)
        return max_val

    # Heapify Down (for deletion)
    def _heapify_down(self, node):
        while node.left:
            largest = node.left
            if node.right and node.right.key > node.left.key:
                largest = node.right

            if node.key < largest.key:
                node.key, largest.key = largest.key, node.key
                node = largest
            else:
                break

    # Heap Sort
    def heapsort(self):
        sorted_list = []
        while self.root:
            sorted_list.append(self.delete())
        return sorted_list

    # Level Order Traversal
    def print_heap(self):
        print([node.key for node in self.nodes])

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
