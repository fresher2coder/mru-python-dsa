from CompleteBinaryTree import CompleteBinaryTree
if __name__ == "__main__":
    binary_tree = CompleteBinaryTree()

    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    for val in data:
        binary_tree.insert_node(val)

    print("Inorder Traversal:")
    binary_tree.inorder_traversal(binary_tree.root)


    binary_tree.delete_node(40)
    print("\nAfter deletion, Inorder Traversal:")
    binary_tree.inorder_traversal(binary_tree.root)


    binary_tree.delete_node(20)
    print("\nAfter deletion, Inorder Traversal:")
    binary_tree.inorder_traversal(binary_tree.root)