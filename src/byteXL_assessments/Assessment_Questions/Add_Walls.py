length = int(input())
nums = [int(n) for n in input().split()]
#nums = list(map(int, input().split()))
k = int(input())
result = []
sum = 0
for n in nums:
    sum += n
    if sum>k:
        result.append(0)
        sum = n
    result.append(n)

for n in result:
    print(n, end=" ")
