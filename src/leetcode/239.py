from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        result = []

        for i in range(len(nums)):

            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)

            if i >= k - 1:
                if queue[0] < i - k + 1:
                    queue.popleft()
                result.append(nums[queue[0]])

        return result
