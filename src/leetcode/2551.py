class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0  # Only one partition, min and max scores are the same

        pairs = [weights[i] + weights[i + 1] for i in range(len(weights) - 1)]
        pairs.sort()

        max_score = sum(pairs[-(k-1):])  # Sum of k-1 largest pairs
        min_score = sum(pairs[:k-1])     # Sum of k-1 smallest pairs

        return max_score - min_score