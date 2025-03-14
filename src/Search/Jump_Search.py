import math

def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n)) #3
    i = step
    prev = 0

    #jump search
    while prev<n and arr[min(i, n) -1] < x: #11, 10
        prev = step
        i += step
        if prev >= n:
            return -1

    #linear
    while prev<min(i, n) and arr[prev]<x:
        prev += 1
        if prev == min(i, n):
            return -1

    return prev if arr[prev]==x else -1;

# Example usage
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] #8 11
x = 60
result = jump_search(arr, x)
print("Element found at index", result if result != -1 else "Element not found")

