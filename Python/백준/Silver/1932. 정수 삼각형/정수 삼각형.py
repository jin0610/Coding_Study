n = int(input())
tri = [list(map(int,input().split())) for _ in range(n)]

dp = [[0] * i for i in range(1, n + 2)]
for i in range(1, n + 1):
    for j in range(i + 1):
        if j == i:
            dp[i][j] = 0
        elif j == 0:
            dp[i][j] = dp[i - 1][j] + tri[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + tri[i - 1][j]

print(max(dp[n]))