import sys
input = sys.stdin.readline

n, k = map(int, input().split())

items = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = items[i - 1]
    for weight in range(1, k + 1):
        if w > weight:
            dp[i][weight] = dp[i-1][weight]
        else:
            dp[i][weight] = max(dp[i-1][weight],  dp[i-1][weight-w] + v)
print(dp[n][k])
