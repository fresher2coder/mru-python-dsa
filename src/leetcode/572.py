class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False

        if root.val != subRoot.val:
            return False

        return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right);