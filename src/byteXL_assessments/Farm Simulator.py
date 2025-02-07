from collections import deque

n = int(input())
crops = [int(crop) for crop in input().split()]

storage = deque()
max = 0
boxes = 0

for crop in crops:

    if crop != -1:
        storage.appendleft(crop)
        boxes += 1

        if boxes > max:
            max = boxes
    else:
        count = 1
        while storage and count <= 3:
            storage.popleft()
            count += 1
            boxes -= 1
else:
    print(max)
    if storage:
        print(*storage)
    else:
        print(-1)

# Background:
# You work on a farm with various crops, each identified by a unique ID. Every day, you harvest one crop type and pack it into boxes, which you store in a storage room. Occasionally, trucks arrive from the city. On those days, you pause harvesting to load up to three of the freshest boxes from storage into the truck. If fewer than three boxes are available, you load however many are there. The trucks prefer the most recently packed boxes of crops.
#
# Objective:
# Write a program to find the maximum amount of storage used at any point in N days and simulate the process to find which crop boxes still remain in the storage room after N days.
#
# Input Format:
# The first line contains an integer N, the number of days.
# The second line contains N integers, where each integer is the crop harvested on that day, and -1 denotes a truck being loaded on that day.
# Output Format:
# Print two lines:
# The first line should be the maximum number of boxes stored over N days.
# The second line should list the available box IDs from freshest to oldest. Print -1 if no boxes remain.
# Constraints:
# 1
# ≤
# ≤ N
# ≤
# ≤ 10
# 5
# 5
#   (number of days)
# Sample input 1:
# 6
# 1 2 8 15 -1 2
#
# Sample output 1:
# 4
# 2 1