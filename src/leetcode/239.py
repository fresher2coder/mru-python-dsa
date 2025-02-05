#Brute Force
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if not nums or k == 0:
            return []

        result = []
        for i in range(n - k + 1):
            result.append(max(nums[i:i + k]))
        return result

# deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q, res = deque(), [] # save index in the queue 'q' (decreasing order)
        for r in range(len(nums)):
            # remove from the right side of the queue all items less than current
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            # while window is not full (size != k) do nothing
            if r+1 < k: continue
            # if most left index out of window [r-k+1, r] we need to remove it
            if q[0] < r-k+1:
                q.popleft()
            # because deque is decreasing the left value is highest
            res.append(nums[q[0]])

        return res