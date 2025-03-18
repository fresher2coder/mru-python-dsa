import heapq
from collections import Counter, deque


class Solution:

    def leastInterval(self, tasks, n):
        # Step 1: Count task frequencies
        task_counts = Counter(tasks)

        # Step 2: Use a max-heap (negate values to simulate max-heap)
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        # Step 3: Initialize time and queue for cooldown
        time = 0
        cooldown_queue = deque()  # Stores (remaining_count, available_time)

        while max_heap or cooldown_queue:
            time += 1

            if max_heap:
                count = -heapq.heappop(max_heap)  # Most frequent task
                if count > 1:
                    # Task still has remaining occurrences, schedule cooldown
                    cooldown_queue.append((count - 1, time + n))

            # Step 4: Check if any task in cooldown can be re-added to heap
            if cooldown_queue and cooldown_queue[0][1] == time:
                heapq.heappush(max_heap, -cooldown_queue.popleft()[0])

        return time



#Solution - formula based
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = list(Counter(tasks).values())
        max_freq = max(task_counts)
        max_freq_count = task_counts.count(max_freq)

        return max(len(tasks), (max_freq - 1) * (n + 1) + max_freq_count)