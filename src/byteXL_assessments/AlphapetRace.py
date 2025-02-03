participants=input()
obstacle=[]
winner=[]
for i in range(len(participants)-1,-1,-1):
  if participants[i]=='0':
    obstacle.append(participants[i])
  else:
    if len(obstacle)!=0:
      obstacle.pop()
    else:
      winner.append(participants[i])
if len(winner)==0:
  print(-1)
else:
  print("".join(winner))



# Background:
# In a mystical world of letters, there exists a grand event known as the "Alphabet Battle." This is not just any ordinary race; it is a race filled with obstacles where only the strongest and most resilient letters can make it to the end. The participants are the letters of the alphabet, and their goal is to navigate a treacherous path filled with hurdles represented by the number '0'. Each letter starts at its initial position and moves to the right at the same speed. When a letter encounters a hurdle, it gets eliminated from the race, and the hurdle is removed, clearing the path for the others.
#
# Objective:
# Your task is to simulate this race and determine which characters manage to complete it. The race track is represented by a string of characters, where each character is either a lowercase letter ('a' to 'z') or a hurdle ('0').
#
# Input Format:
# The input to your program consists of data representing the intervals start and end:
#
# The first line and only line of input is a lowercase string representing the starting points of the alphabets and the hurdles locations.
# Output Format:
# Print a string representing the winners in the order they finish from left to right. If no one finishes the race, print -1.