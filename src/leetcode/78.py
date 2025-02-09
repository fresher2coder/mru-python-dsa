# RECURSION

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, subset):
            result.append(subset[:])

            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

        backtrack(0, [])
        return result
    
# ITERATION
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]  # Start with an empty subset

        for num in nums:
            # Add current element to all existing subsets
            result += [subset + [num] for subset in result]
            print(result)

        return result