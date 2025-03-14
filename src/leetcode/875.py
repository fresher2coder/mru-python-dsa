class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            total_hours = sum((pile + mid - 1) // mid for pile in piles)  # Optimized

            if total_hours <= h:
                right = mid  # Try smaller speed
            else:
                left = mid + 1  # Increase speed

        return left  # Minimum speed found
