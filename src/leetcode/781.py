from math import ceil
from collections import Counter


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        rabbits = 0

        for answer, freq in count.items():
            group_size = answer + 1
            groups = ceil(freq / group_size)  # Ceiling division
            rabbits += groups * group_size

        return rabbits
