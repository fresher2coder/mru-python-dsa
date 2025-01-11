numbers = [4, 1, 3, 9, 2]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # Output: [9, 4, 3, 2, 1]

# Using list.sort()
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 4, 3, 2, 1]

words = ["apple", "cat", "banana", "pear"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # Output: ['cat', 'pear', 'apple', 'banana']

# Using list.sort()
words.sort(key=len)
print(words)  # Output: ['cat', 'pear', 'apple', 'banana']

# Sort tuples by the second element
data = [(1, 3), (4, 1), (2, 2)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [(4, 1), (2, 2), (1, 3)]

# Sort strings by length in descending order
words = ["apple", "cat", "banana", "pear"]
sorted_words = sorted(words, key=len, reverse=True)
print(sorted_words)  # Output: ['banana', 'apple', 'pear', 'cat']

data = [
    {"name": "Dineshkumar", "info": {"age": 25, "score": 90}},
    {"name": "Divya Dineshkumar", "info": {"age": 25, "score": 85}},
    {"name": "Darwin Divya Dinesh", "info": {"age": 20, "score": 95}},
]

# Sort by age, then by score
sorted_data = sorted(data, key=lambda x: (x["info"]["age"], x["info"]["score"]))
print(sorted_data)
# Output: [{'name': 'Darwin Divya Dinesh', 'info': {'age': 20, 'score': 95}}, 
#          {'name': 'Divya Dineshkumar', 'info': {'age': 25, 'score': 85}}, 
#          {'name': 'Dineshkumar', 'info': {'age': 25, 'score': 90}}]

def custom_key(item):
    return item["info"]["age"], -item["info"]["score"]  # Sort by age, then descending score

sorted_data = sorted(data, key=custom_key)
print(sorted_data)
# Output: [{'name': 'Darwin Divya Dinesh', 'info': {'age': 20, 'score': 95}}, 
#          {'name': 'Dineshkumar', 'info': {'age': 25, 'score': 90}}, 
#          {'name': 'Divya DIneshkumar', 'info': {'age': 25, 'score': 85}}]
