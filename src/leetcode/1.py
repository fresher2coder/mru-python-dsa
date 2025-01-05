#Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        length = len(nums)
        numDict = {}

        for i in range(length):

            c = target - nums[i]
            if c in numDict:
                return [numDict[c], i]
            numDict[nums[i]] = i
        return []