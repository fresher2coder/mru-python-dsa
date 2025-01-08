# Creating an empty list
my_list = []

# Creating a list with elements
my_list = [1, 2, 3, 'a', 'b', True]

# Reading a single-line input from the user
input_str = input("Enter elements (space-separated): ")
user_list = input_str.split()  # Splits the input string into a list of words
print("Your list:", user_list)

# Reading multiple lines of input until a stop condition is met
user_list = []
print("Enter elements (type 'done' to stop):")
while True:
    element = input()
    if element.lower() == 'done':
        break
    user_list.append(element)

print("Your list:", user_list)

my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

# list-comprehension
squared_list = [x**2 for x in my_list]
print(squared_list)

#enumerate - index and element during traversal
for index, value in enumerate(my_list):
    print(f"Index {index}: Value {value}")

#type-conversion
# Convert a list of strings to integers
str_list = ['1', '2', '3']
int_list = [int(x) for x in str_list]
print(int_list)

# Convert a list of integers to strings
num_list = [1, 2, 3]
str_num_list = [str(x) for x in num_list]
print(str_num_list)

#in-built methods
# Initialize a list with some values
my_list = [1, 2, 3, 4, 5]

# 1. append() - Adds an element to the end of the list
my_list.append(6)  # [1, 2, 3, 4, 5, 6]
print("After append:", my_list)  # Time Complexity: O(1)

# 2. index() - Returns the index of the first occurrence of the value
index_of_3 = my_list.index(3)  # Returns 2 (index of 3)
print("Index of 3:", index_of_3)  # Time Complexity: O(n)

# 3. clear() - Removes all elements from the list
my_list.clear()  # [] (empties the list)
print("After clear:", my_list)  # Time Complexity: O(n)

# Reinitialize the list
my_list = [1, 2, 3, 4, 5, 6]

# 4. insert() - Inserts an element at a specific position
my_list.insert(2, 10)  # [1, 2, 10, 3, 4, 5, 6]
print("After insert:", my_list)  # Time Complexity: O(n)

# 5. count() - Returns the number of occurrences of a value
count_of_5 = my_list.count(5)  # Returns 1 (since 5 appears once)
print("Count of 5:", count_of_5)  # Time Complexity: O(n)

# 6. copy() - Returns a shallow copy of the list
copied_list = my_list.copy()  # [1, 2, 10, 3, 4, 5, 6]
print("Copied list:", copied_list)  # Time Complexity: O(n)

# 7. extend() - Extends the list by adding all elements from another iterable
my_list.extend([7, 8, 9])  # [1, 2, 10, 3, 4, 5, 6, 7, 8, 9]
print("After extend:", my_list)  # Time Complexity: O(k), where k is the length of the iterable

# Reinitialize the list
my_list = [1, 2, 3, 4, 5, 6]

# 8. pop() - Removes and returns the element at the specified index (or the last element by default)
popped_element = my_list.pop()  # Removes 6
print("After pop:", my_list)  # Time Complexity: O(1) if popping the last element, O(n) if popping from the middle

# 9. remove() - Removes the first occurrence of the specified value
my_list.remove(4)  # [1, 2, 3, 5]
print("After remove:", my_list)  # Time Complexity: O(n)

# 10. reverse() - Reverses the elements of the list
my_list.reverse()  # [5, 3, 2, 1]
print("After reverse:", my_list)  # Time Complexity: O(n)

# 11. sort() - Sorts the list in ascending order (in-place)
my_list.sort()  # [1, 2, 3, 5]
print("After sort:", my_list)  # Time Complexity: O(n log n)

# append(x) – Adds an element to the end of the list.

# Time Complexity: O(1) (amortized)
# index(x) – Returns the index of the first occurrence of the value x.

# Time Complexity: O(n) (in the worst case, it checks each element)
# clear() – Removes all elements from the list.

# Time Complexity: O(n) (because it needs to iterate through all elements to remove them)
# insert(i, x) – Inserts an element x at the index i.

# Time Complexity: O(n) (because it may require shifting elements after index i)
# count(x) – Returns the number of occurrences of x in the list.

# Time Complexity: O(n) (it needs to check every element)
# copy() – Returns a shallow copy of the list.

# Time Complexity: O(n) (it creates a new list and copies the elements)
# extend(iterable) – Adds all elements from another iterable to the end of the list.

# Time Complexity: O(n), where n is the number of classes in the MRO (applicable in class inheritance)
# pop(i) – Removes and returns the element at index i (or the last element by default).

# Time Complexity: O(1) (if popping the last element), O(n) (if popping an element from the middle, since the subsequent elements need to be shifted)
# remove(x) – Removes the first occurrence of the value x.

# Time Complexity: O(n) (it may need to search for the value)
# reverse() – Reverses the elements of the list in-place.

# Time Complexity: O(n) (it needs to iterate through all the elements)
# sort() – Sorts the list in-place.
# Time Complexity: O(n log n) (this is due to the Timsort algorithm used by Python’s sort())