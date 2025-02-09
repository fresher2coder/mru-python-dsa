class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start, subset):
            # Base case: combination of size k found
            if len(subset) == k:
                result.append(subset[:])
                return

            for i in range(start, n + 1):
                subset.append(i)
                backtrack(i + 1, subset)
                subset.pop()

        backtrack(1, [])
        return result