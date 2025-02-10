class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(remaining, path, start):
            # Base case: when remaining sum is 0
            if remaining == 0:
                result.append(path[:])
                return

            # Iterate through the candidates
            for i in range(start, len(candidates)):
                # Skip the number if it exceeds the remaining target
                if candidates[i] > remaining:
                    continue

                # Include the candidate and move forward with reduced target
                path.append(candidates[i])
                backtrack(remaining - candidates[i], path, i)
                path.pop()  # Backtrack step

        backtrack(target, [], 0)
        return result