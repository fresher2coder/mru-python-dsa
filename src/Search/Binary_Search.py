def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid  # Element found
        elif arr[mid] < x:
            left = mid + 1  # Search in right half
        else:
            right = mid - 1  # Search in left half
    return -1  # Element not found

def binary_search_recursive(arr, left, right, x):
    if left > right:
        return -1  # Base case: Element not found
    mid = left + (right - left) // 2
    if arr[mid] == x:
        return mid  # Element found
    elif arr[mid] < x:
        return binary_search_recursive(arr, mid + 1, right, x)  # Right half
    else:
        return binary_search_recursive(arr, left, mid - 1, x)  # Left half

# Example usage
arr = [10, 20, 30, 40, 50]
x = 30
result = binary_search(arr, x)
print("Element found at index", result if result != -1 else "Element not found")

result = binary_search_recursive(arr, 0, len(arr) - 1, x)
print("Element found at index", result if result != -1 else "Element not found")
