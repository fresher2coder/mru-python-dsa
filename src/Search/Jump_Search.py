import math

def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))  # Block size to jump
    prev = 0

    # Jump in blocks until we exceed the search element
    while prev < n and arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1  # Element not found

    # Linear search within the block
    while prev < min(step, n) and arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1  # Element not found

    return prev if arr[prev] == x else -1

# Example usage
arr = [10, 20, 30, 40, 50]
x = 30
result = jump_search(arr, x)
print("Element found at index", result if result != -1 else "Element not found")
