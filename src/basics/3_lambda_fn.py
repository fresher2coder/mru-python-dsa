# lambda arguments: expression

# A simple lambda function to double a number
double = lambda x: x * 2
print(double(5))  # Output: 10


# map(function, iterable)
# Double each number in a list
numbers = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, numbers)
print(list(doubled))  # Output: [2, 4, 6, 8, 10]

# 1. Map Example: Convert Temperatures
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda x: (x * 9/5) + 32, celsius))
print(fahrenheit)  # Output: [32.0, 50.0, 68.0, 86.0]

# filter(function, iterable)
# Filter even numbers from a list
numbers = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # Output: [2, 4]

# 2. Filter Example: Names Starting with "A"
names = ["Alice", "Bob", "Anna", "Charlie"]
a_names = list(filter(lambda name: name.startswith('A'), names))
print(a_names)  # Output: ['Alice', 'Anna']


# reduce(function, iterable)

from functools import reduce

# Calculate the product of all numbers in a list
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24

# 3. Reduce Example: Longest Word

words = ["apple", "banana", "cherry", "blueberry"]
longest = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(longest)  # Output: blueberry

