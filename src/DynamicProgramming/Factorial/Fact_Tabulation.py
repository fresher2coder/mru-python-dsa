import sys

# Increase limit to allow large factorial values
# sys.set_int_max_str_digits(100000)

def factorial_tabulation(n):
    dp = [1] * (n + 1)  # Initialize DP table
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] * i  # Bottom-Up Calculation
    return dp[n]

print(factorial_tabulation(1000))
print(factorial_tabulation(20000))  # Works fine now
