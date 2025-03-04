def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):  # Find the smallest element in remaining array
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap with first unsorted element
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Selection Sort:", selection_sort(arr))
