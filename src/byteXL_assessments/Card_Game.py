from collections import deque


def count_cards(N, powers, k):
    deck = deque()
    for power in powers:
        if deck and power > deck[-1]:
            deck.popleft()
        deck.append(power)

    count = sum(1 for card in deck if card >= k)
    print(count)


N = int(input())
powers = list(map(int, input().split()))
k = int(input())
count_cards(N, powers, k)

# Background:
# In a card game tournament, you have N playing cards, each representing the power of a player. You place each card into a deck (from left to right). The deck has a specific rule:
#
# If a new card has a higher power than the card at the bottom of the deck, remove the bottom-most card from the deck and place the new card on top.
# Otherwise, just add the new card on top of the deck without removing any card.
# Objective:
# Your task is to find the number of cards left in the deck that have a power greater than or equal to a given integer k after placing all the cards following the above rules.
#
# Input Format:
# The first line contains an integer N, the number of cards.
# The second line contains N space-separated integers representing the power of each card.
# The third line contains an integer k.
# Output Format:
# Print the number of cards left in the deck that have a power greater than or equal to k.
#
# Constraints:
# 1 < N ≤ 1000
# 0 ≤ A[i] ≤ 1000
# 0 < k < N
#
# Sample Input 1:
# 6
# 1 6 9 5 3 10
# 2
#
# Sample Output 1:
# 3