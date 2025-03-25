def knapsack_01(W, wt, val, N):
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], val[i - 1] + dp[i - 1][w - wt[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    # Print DP table for debugging
    # print("DP Table:")
    # for row in dp:
    #     print(row)

    return dp[N][W]


#Optimizded
def knapsack_01_opt(W, wt, val, N):
    dp = [0] * (W + 1)  # Single row DP table

    for i in range(N):
        for w in range(W, wt[i] - 1, -1):  # Iterate backwards
            dp[w] = max(dp[w], val[i] + dp[w - wt[i]])

    return dp[W]

