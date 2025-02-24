from AVL import AVLTree

# Example usage:
avl = AVLTree()
root = None

# Inserting elements
for key in [9, 5, 10, 0, 6, 11, -1, 1, 2]:
    root = avl.insert(root, key)

print("Inorder traversal after insertion:")
avl.inorder(root)
print()

# Deleting elements
for key in [10, 0, 2]:
    root = avl.delete(root, key)

print("Inorder traversal after deletion:")
avl.inorder(root)
print()

# Searching for a key
search_key = 1
result = avl.search(root, search_key)
if result:
    print(f"Key {search_key} found in the AVL tree.")
else:
    print(f"Key {search_key} not found in the AVL tree.")
