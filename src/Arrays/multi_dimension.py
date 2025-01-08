# Creating a 3D array (list of lists of lists)
arr3D = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

# Traversing a 3D array
for matrix in arr3D:
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()
    print()
