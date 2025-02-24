# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum = 0
# 1 2 3 4 5 6 7 8 9 10
        def sumBST(root, low, high):

            if not root:
                return

            if root.val > low:
                sumBST(root.left, low, high)

            #root
            if root.val>=low and root.val<=high:
                self.sum += root.val

            if root.val < high:
                sumBST(root.right, low, high)

        sumBST(root, low, high)
        return self.sum