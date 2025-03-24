# solution 1: recursion
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def lcs_recursive(text1, text2, m, n):
            if m == 0 or n == 0:
                return 0
            if text1[m - 1] == text2[n - 1]:
                return 1 + lcs_recursive(text1, text2, m - 1, n - 1)
            else:
                return max(lcs_recursive(text1, text2, m - 1, n), lcs_recursive(text1, text2, m, n - 1))

        return lcs_recursive(text1, text2, len(text1), len(text2))

#solution 2: DP memorization
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def lcs_memo(text1, text2, m, n, dp):
            if m == 0 or n == 0:
                return 0
            if dp[m][n] != -1:  # If already computed, return cached result
                return dp[m][n]

            if text1[m - 1] == text2[n - 1]:
                dp[m][n] = 1 + lcs_memo(text1, text2, m - 1, n - 1, dp)
            else:
                dp[m][n] = max(lcs_memo(text1, text2, m - 1, n, dp), lcs_memo(text1, text2, m, n - 1, dp))

            return dp[m][n]

        m, n = len(text1), len(text2)
        dp = [[-1] * (n + 1) for _ in range(m + 1)]  # Create memoization table
        return lcs_memo(text1, text2, m, n, dp)


# solution 3: dp tabulation
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # DP table

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]

#solution 4: optimized
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        prev = [0] * (n + 1)  # Previous row
        curr = [0] * (n + 1)  # Current row

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr[:]  # Move current row to previous row

        return prev[n]
