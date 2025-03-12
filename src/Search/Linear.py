def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # Element found
    return -1  # Element not found

# Example usage
arr = [10, 20, 30, 40, 50]
x = 30
result = linear_search(arr, x)
print("Element found at index", result if result != -1 else "Element not found")
