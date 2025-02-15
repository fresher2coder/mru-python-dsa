from BST import BinarySearchTree

if __name__ == "__main__":
    bst = BinarySearchTree()
    TreeNodes = [50, 30, 20, 40, 70, 60, 80]

    for TreeNode in TreeNodes:
        bst.insert(TreeNode)

    print("Inorder Traversal:", bst.inorder())
    print("Preorder Traversal:", bst.preorder())
    print("Postorder Traversal:", bst.postorder())
    print("Level Order Traversal:", bst.levelorder())

    key_to_search = 40
    print(f"Search {key_to_search}:", "Found" if bst.search(key_to_search) else "Not Found")

    key_to_delete = 50
    bst.delete(key_to_delete)
    print(f"After deleting {key_to_delete}, Inorder Traversal:", bst.inorder())
