class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1  # Base case: One way to make amount 0 (use no coins)

        for coin in coins:  # Process each coin one by one
            for w in range(coin, amount + 1):
                dp[w] += dp[w - coin]  # Add ways to make (w - coin)

        return dp[amount]