from collections import deque
nums = [int(n) for n in input().split()]
k = int(input())
window = 0
result = []

for i in range(len(nums)):
    #form the current window
    if i < k:
        window += nums[i]
    else:
        result.append(window)
        window = window + nums[i] - nums[i-k]
        result.append(window)
else:
    print(*result)
