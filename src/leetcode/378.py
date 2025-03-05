class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]

        def count_less_equal(mid):
            count, j = 0, n - 1
            for i in range(n):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += (j + 1)
            return count

        while left < right:
            mid = (left + right) // 2
            if count_less_equal(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left

