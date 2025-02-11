from collections import deque
from TreeNode import TreeNode

class CompleteBinaryTree:
    def __init__(self):
        self.root = None
        self.queue = deque()

    def create_node(self, val):
        return TreeNode(val)

    def parent_insertion(self, root):
        if root.right is None:
            return root

        self.queue.append(root.left)
        self.queue.append(root.right)
        return self.parent_insertion(self.queue.popleft())

    def insert_node(self, val):
        if self.root is None:
            self.root = self.create_node(val)
            return
        self.queue.clear()  # Reset the queue
        parent = self.parent_insertion(self.root)

        if parent.left is None:
            parent.left = self.create_node(val)
        elif parent.right is None:
            parent.right = self.create_node(val)


    def inorder_traversal(self, root):
        if root is None:
            return

        self.inorder_traversal(root.left)
        print(root.val, end=" ")
        self.inorder_traversal(root.right)

    def search(self, root, key):
        if root is None:
            return None

        if root.val == key:
            return root

        self.queue.append(root.left)
        self.queue.append(root.right)
        return self.search(self.queue.popleft(), key)

    def right_most_node(self, root, prev=None):
        if root.left is None:
            return prev

        if root.right is None:
            return root

        self.queue.append(root.left)
        self.queue.append(root.right)
        return self.right_most_node(self.queue.popleft(), root)

    def delete_node(self, key):
        if self.root is None:
            return

        self.queue.clear()
        del_node = self.search(self.root, key)
        if del_node is None:
            print(f"{key} is not found")
            return

        self.queue.clear()  # Reset the queue
        last_parent = self.right_most_node(self.root, None)

        if last_parent.right is not None:
            del_node.val = last_parent.right.val
            last_parent.right = None
        else:
            del_node.val = last_parent.left.val
            last_parent.left = None

