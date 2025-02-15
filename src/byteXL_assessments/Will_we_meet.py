def solve():
  n,q = map(int,input().split())
  h=list(map(int,input().split()))
  for _ in range(q):
    j,m = map(int,input().split())
    ans = -1
    for i in range(n):
      if(i>j and h[i] > h[j] or i==j)and(i>m and h[i]>h[m]or i==m):
        ans=i if ans==-1 or i<ans else ans
    print(ans,end=" ")
  print()
solve()

# Background:
# Jatin and Mano are two friends living in the same lane with N buildings, where the ith building is of height h[i]. Now, given an array (0-based indexing) h, representing the heights of the buildings. Jatin and Mano try different starting positions and they want to determine if they’ll meet or not. Trying these positions and jumping through the building will be a hectic task for both of them. So, they need your help, and they’ll tell you their starting position as a query [j, m], where j is the starting index of Jatin’s building and m is the starting index of Mano’s building.
#
# Now, there is one rule when going from one building to another building, i.e., moving from building at index x to building at index y can only be done if and only if both x < y and h[x] < h[y].
#
# Objective:
# Write a program to process Q queries, each printing the index of the leftmost possible building they can meet, if it’s not possible for them to meet If it’s impossible, then print -1 in that.
#
# Input Format:
# The first line of input contains two integers N the number of buildings in the city and Q the number of queries.
# The next line contains N space-separated integers representing the heights of the buildings.
# The next Q lines contain 2 space-separated integers J and M.
# Output Format:
# You need to output the leftmost possible index of the building for each query as a space-separated integer, where both of Jatin and Mano can meet. If the meeting is impossible, print(-1).
# You need to print Q integers separated by a space, where the i
# t
# h
# th
#   integer represents the answer for the i
# t
# h
# th
#   query.
# Constraints:
# 1 ≤ N, Q ≤ 200000
# 1 ≤ J, M ≤ N
# Sample Input 1:
# 6 5
# 6 4 8 5 2 7
# 0 1
# 0 3
# 2 4
# 3 4
# 2 2
#
# Sample Output 1:
# 2 5 -1 5 2