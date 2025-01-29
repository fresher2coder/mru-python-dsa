m = int(input())
prices = [int(n) for n in input().split()]
total_bill = 0
for _ in range(m):
    index, quantity, discount = map(int, input().split())
    discounted_price = prices[index] * (1 - discount / 100)
    total_bill += discounted_price * quantity

print(int(total_bill))

