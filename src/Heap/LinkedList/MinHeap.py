class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None  # To track parent for heapify-up

class MinHeap:
    def __init__(self):
        self.root = None
        self.nodes = []  # To store nodes in level order for easy insertion

    # Insert element into heap
    def insert(self, key):
        new_node = Node(key)
        if not self.root:
            self.root = new_node
        else:
            parent = self.nodes[(len(self.nodes) - 1) // 2]  # Find parent using level-order indexing
            if not parent.left:
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent
            self._heapify_up(new_node)
        self.nodes.append(new_node)

    # Heapify Up (for insertion)
    def _heapify_up(self, node):
        while node.parent and node.key < node.parent.key:
            node.key, node.parent.key = node.parent.key, node.key
            node = node.parent

    # Extract min (delete root)
    def delete(self):
        if not self.root:
            return None
        if len(self.nodes) == 1:
            min_val = self.root.key
            self.root = None
            self.nodes.pop()
            return min_val

        min_val = self.root.key
        last_node = self.nodes.pop()  # Get last inserted node
        if last_node.parent:
            if last_node.parent.right == last_node:
                last_node.parent.right = None
            else:
                last_node.parent.left = None

        self.root.key = last_node.key  # Replace root with last node's value
        self._heapify_down(self.root)
        return min_val

    # Heapify Down (for deletion)
    def _heapify_down(self, node):
        while node.left:
            smallest = node.left
            if node.right and node.right.key < node.left.key:
                smallest = node.right

            if node.key > smallest.key:
                node.key, smallest.key = smallest.key, node.key
                node = smallest
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
