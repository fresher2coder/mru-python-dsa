# Save this in a file called hello.py
print("Welcome to Python Programming!")

#data-type
age = 25  # Integer
price = 99.99  # Float
complex_num = 3 + 4j  # Complex number
name = "John Doe"
fruits = ["apple", "banana", "cherry"]
coordinates = (10.5, 20.8)
numbers = range(5)  # Creates a range from 0 to 4
unique_numbers = {1, 2, 3, 3, 2}
frozen_set = frozenset({1, 2, 3})
person = {"name": "Alice", "age": 30}
is_python_fun = True
byte_data = b"Hello"
nothing = None

# Single-line comment
# This program calculaq of a number

number = int(input("Enter a number: "))  # User input
square = number ** 2
print(f"The square of {number} is {square}.")  # Formatted output

#if-else
age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("Congratulations on becoming an adult!")
else:
    print("You are an adult.")


#loops
# Print all even numbers from 1 to 10
for num in range(1, 11):
    if num % 2 == 0:
        print(num, end=" ")

# Using while loop
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1


#functions
#Positional arguments → Default arguments → *args → **kwargs
def show_details(name, age=18, *hobbies, **other_details):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print("Hobbies:", ", ".join(hobbies))
    for key, value in other_details.items():
        print(f"{key}: {value}")

show_details("Alice", 25, "Reading", "Traveling", city="Paris", job="Engineer")

#list-comprehension
#[expression for item in iterable if condition]
#1. Creating a List
squares = [x**2 for x in range(1, 11)]
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 2. Filtering with Conditions
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # Output: [2, 4, 6, 8, 10]

# 3. Transforming Items
words = ["apple", "banana", "cherry"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  # Output: ['APPLE', 'BANANA', 'CHERRY']

# 4. Nested Loops
coordinates = [(x, y) for x in range(1, 4) for y in range(1, 3)]
print(coordinates)  # Output: [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]

# 5. Conditional Expression in Output
labels = ["even" if x % 2 == 0 else "odd" for x in range(1, 6)]
print(labels)  # Output: ['odd', 'even', 'odd', 'even', 'odd']

# 6. Flattening a Nested List
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = [num for sublist in nested_list for num in sublist]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]

# 8. Filtering with Strings
text = "hello world"
vowels = [char for char in text if char in "aeiou"]
print(vowels)  # Output: ['e', 'o', 'o']

#dist-comprehension
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)  # Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

original = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {value: key for key, value in original.items()}
print(reversed_dict)  # Output: {1: 'a', 2: 'b', 3: 'c'}

classification = {x: "even" if x % 2 == 0 else "odd" for x in range(1, 6)}
print(classification)  # Output: {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

#set-comprehension
unique_chars = {char for char in "hello world"}
print(unique_chars)  # Output: {'d', 'e', 'h', 'l', 'o', 'r', 'w'}













