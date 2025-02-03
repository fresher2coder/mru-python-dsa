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



# Objective:
# You will be given a string and you can delete two adjacent characters in the string any number of times. You need to find the longest famous string you can create using the string and perform the operation from the right and print the reverse of it.
#
# Input Format:
# The input to your program consists of the string:
#
# The first line contains an integer N, representing the length of the string.
# The second line contains a string of length N.
# Output Format:
# Output a string which is the reverse of the longest famous string you can create by performing the specified operation any number of times on the input string.