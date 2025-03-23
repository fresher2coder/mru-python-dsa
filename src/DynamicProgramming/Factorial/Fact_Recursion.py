import sys

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)  # Recursive call

# Uncomment to see Stack Overflow
# sys.setrecursionlimit(100000)  # Increase recursion limit (not recommended)
print(factorial(10))  # Works fine
# print(factorial(20000))  # ❌ Causes RecursionError
