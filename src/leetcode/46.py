class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start=0):
            # Base case: If all positions are fixed, add to result
            if start == len(nums):
                result.append(nums[:])
                return

            for i in range(start, len(nums)):
                # Swap to include nums[i] in the current permutation
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                # Undo the swap for backtracking
                nums[start], nums[i] = nums[i], nums[start]

        backtrack()
        return result