# Creating a 2D array (list of lists)
arr2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Traversing (printing elements)
for row in arr2D:
    for element in row:
        print(element, end=" ")
    print()

# Accessing element at row 1, column 2
print("Element at row 1, column 2:", arr2D[1][2])

# Insertion (adding a row or column)
arr2D.append([10, 11, 12])  # Adding a new row
arr2D[0].append(4)  # Adding an element to the first row
print("Array after insertion:", arr2D)

# Deletion (removing a row or column)
arr2D.pop(0)  # Remove the first row
print("Array after deletion:", arr2D)
