def knapsack_01(W, wt, val, N):
    dp = [[0] * (W+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for w in range(1, W+1):
            #include or exclude
            if wt[i-1] > w:
                #exclude - prev value
                dp[i][w] = dp[i-1][w]
            else:
                #include
                dp[i][w] = max(dp[i-1][w], val[i-1] + dp[i-1][w-wt[i-1]])
    return dp[N][W]



#Optimizded
def knapsack_01_opt(W, wt, val, N):
    dp = [0] * (W + 1)  # Single row DP table

    for i in range(N):
        for w in range(W, wt[i] - 1, -1):  # Iterate backwards
            dp[w] = max(dp[w], val[i] + dp[w - wt[i]])

    return dp[W]

