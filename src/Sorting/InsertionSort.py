def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:  # Shift elements to the right
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Insertion Sort:", insertion_sort(arr))
