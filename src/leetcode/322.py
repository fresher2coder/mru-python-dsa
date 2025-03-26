class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)  # Initialize with large values
        dp[0] = 0  # Base case: 0 coins needed for amount 0

        for coin in coins:  # Iterate over coin denominations
            for w in range(coin, amount + 1):  # Process amounts in increasing order
                dp[w] = min(dp[w], 1 + dp[w - coin])  # Pick the coin and update

        return dp[amount] if dp[amount] != float('inf') else -1  # Return result