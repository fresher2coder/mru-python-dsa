# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 1-3(2) 2-2(1) 3-1(0) 4 5 6 7 8 9 10
        self.count = 0
        self.result = None

        def findSmallest(root, k):

            if not root or self.result is not None:
                return

            findSmallest(root.left, k)

            self.count += 1
            if k == self.count:
                self.result = root.val
                return

            findSmallest(root.right, k)

        findSmallest(root, k)
        return self.result
