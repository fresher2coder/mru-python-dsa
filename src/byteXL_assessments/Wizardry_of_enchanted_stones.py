from collections import deque


def find_last_stone(N, stones):
    queue = deque(stones)
    turn = 0

    while len(queue) > 1:
        if turn == 0:
            queue.append(queue.popleft())
            queue.popleft()
        else:
            queue.append(queue.popleft())
            queue.append(queue.popleft())
            queue.popleft()
        turn = 1 - turn
    print(turn, queue[0])


N = int(input())
stones = list(map(int, input().split()))
find_last_stone(N, stones)

# Background:
# In the magical kingdom of Numeria, there are two wizards, Zara and Leo, who are known for their incredible mastery over numbers. One day, the grand wizard Elara challenges them with a task to test their skills.
# The challenge involves manipulating a pile of enchanted stones, each bearing a number. There are two distinct magical spells they can cast on the pile:
#
# Translocate Spell: Move the top stone to the bottom of the pile.
# Vanish Spell: Remove the top stone from the pile permanently.
# Zara, being the more experienced wizard, goes first. She casts the Translocate Spell once and then the Vanish Spell once during her turn. Leo follows by casting the Translocate Spell twice and then the Vanish Spell once during his turn.
# The wizards take turns alternately, starting with Zara. They continue until only one stone is left in the pile. Wizard Zara is denoted by 1 while wizard Leo is denoted by 0.
#
# Objective:
# The goal is to determine which wizard casts the final spell and to identify the number on the last remaining enchanted stone.
#
# Input Format:
# The first line contains N, the number of stones in the pile.
# The second line contains N space-separated integers representing the numbers in the pile of stones initially (top to bottom).
# Output Format:
# Print two space-separated integers:
#
# The identifier for the wizard who makes the last move (1 for Zara and 0 for Leo).
# The number written on the last stone left.

# Sample input 1:
# 3
# -5 0 -5
#
# Sample output 1:
# 0 -5