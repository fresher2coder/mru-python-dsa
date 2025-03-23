def fib_memo(n, memo={}):
    if n in memo:  # Check if result is already computed
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)  # Store result in memo
    return memo[n]

print(fib_memo(10))  # Output: 55
print(fib_memo(100))  # Output: 354224848179261915075 (Efficiently computed)
