def fib_tabulation(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)  # Create DP table
    dp[1] = 1  # Base case
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # Compute Fibonacci iteratively
    return dp[n]

print(fib_tabulation(10))  # Output: 55
print(fib_tabulation(100))  # Output: 354224848179261915075
