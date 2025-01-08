# Creating a 1D array (list)
arr = [1, 2, 3, 4, 5]

# Traversing (printing elements)
for element in arr:
    print(element)

# Searching (find if 3 exists)
if 3 in arr:
    print("Found 3")
else:
    print("3 not found")

# Insertion (adding a value at a specific position)
arr.insert(2, 6)  # Insert 6 at index 2
print("Array after insertion:", arr)

# Deletion (removing a value by index or by value)
arr.remove(4)  # Remove the first occurrence of 4
arr.pop(1)  # Pop element at index 1
print("Array after deletion:", arr)

# Sorting
arr.sort()  # Sort in ascending order
print("Array after sorting:", arr)
