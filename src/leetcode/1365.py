class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)  # Step 1: Sort array
        num_map = {}  # Step 2: Store first occurrence index

        for i, num in enumerate(sorted_nums):
            if num not in num_map:
                num_map[num] = i  # First occurrence in sorted array

        return [num_map[num] for num in nums]  # Step 3: Lookup index