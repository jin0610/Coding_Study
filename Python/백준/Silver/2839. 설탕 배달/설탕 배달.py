import sys
inf = sys.maxsize

N = int(input())
dp = [inf] * (max(5, N) + 1)

dp[3] = 1
dp[4] = inf
dp[5] = 1

for n in range(5, N + 1):
    dp[n] = min(dp[n], dp[n - 3] + 1, dp[n-5] + 1)

if dp[N] != inf:
    print(dp[N])
else:
    print(-1)