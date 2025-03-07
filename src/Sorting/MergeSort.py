def merge(arr, left, mid, right): #arr, 0, 4, 9,
    n1 = mid - left + 1  # left to mid 0 4
    n2 = right - mid     # mid+1 to right 5 9

    L = arr[left:mid+1]   # Left subarray
    R = arr[mid + 1:right + 1]  # Right subarray

    i, j, k = 0, 0, left

    # Merge the two subarrays
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy remaining elements from L[], if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy remaining elements from R[], if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2
        # pi
        merge_sort(arr, left, mid) #quickSort(arr, low, pi-1)
        merge_sort(arr, mid+1, right) #quickSort(arr, pi+1 , high)

        merge(arr, left, mid, right)

def print_array(arr):
    print(" ".join(map(str, arr)))

# Example Usage
arr = [45, 56, 7, 15, 34, 29, 61, 8, 14, 10]
print("Original array:")
print_array(arr)

merge_sort(arr, 0, len(arr) - 1)

print("\nSorted array:")
print_array(arr)
