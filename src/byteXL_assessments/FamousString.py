def is_same_type(a,b):
  if a.isalpha() and b.isalpha():
    return True
  if a.isdigit() and b.isdigit():
    return True
  if not a.isalnum() and not b.isalnum():
    return True
  return False
n=int(input())
string=input()
stack=[]
for char in string:
  if stack and is_same_type(stack[-1],char):
    stack.pop()
  else:
    stack.append(char)
if stack:
  print("".join(stack[::-1]))

# Background:
# There are some strings which are called famous strings which follow some common rules. The rules are:
#
# No two letters should be adjacent.
# No two special symbols should be adjacent. (Any character which is not a letter or an integer is considered a special symbol)
# No two integers should be adjacent.
# In other words, we can say that no two similar characters should be present adjacent in the string for a string to be famous.
# Objective:
# You will be given a string and you can delete two adjacent characters in the string any number of times. You need to find the longest famous string you can create using the string and perform the operation from the right and print the reverse of it.