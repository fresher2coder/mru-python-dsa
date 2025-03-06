def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1

        while left <= right and arr[right] >= pivot:
            right -= 1

        if left >= right:
            break

        swap(arr, left, right)

    swap(arr, low, right)
    return right

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def print_array(arr):
    print(" ".join(map(str, arr)))

# Example usage
arr = [45, 56, 7, 15, 34, 29, 61, 8, 14, 10]
n = len(arr)

print("Unsorted Array:")
print_array(arr)

quick_sort(arr, 0, n - 1)

print("Sorted Array:")
print_array(arr)

