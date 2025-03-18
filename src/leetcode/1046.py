import heapq


class Solution:

    def lastStoneWeight(self, stones):
        # Convert to max-heap by pushing negative values
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            # Extract the two heaviest stones
            stone1 = -heapq.heappop(max_heap)  # Largest
            stone2 = -heapq.heappop(max_heap)  # Second Largest

            # If they are not equal, push the difference back
            if stone1 != stone2:
                heapq.heappush(max_heap, -(stone1 - stone2))

        # Return the last stone weight (or 0 if no stones left)
        return -max_heap[0] if max_heap else 0



