class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero_index, two_index, i = 0, len(nums) - 1, 0

        while i <= two_index:
            if nums[i] == 2:
                nums[i], nums[two_index] = nums[two_index], nums[i]
                two_index -= 1
            else:
                if nums[i] == 0:
                    nums[i], nums[zero_index] = nums[zero_index], nums[i]
                    zero_index += 1
                i += 1
