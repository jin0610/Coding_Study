N = 0

def solution(triangle):
    global N
    
    N = len(triangle)
    dp = [[0 for _ in range(N)] for _ in range(N)]
    
    # 아래, 우측 대각선
    dirs = [(1, 0), (1, 1)]
    
    dp[0][0] = triangle[0][0]
    
    for x in range(N - 1):
        for y in range(x + 1):
            for dx, dy in dirs:
                dp[x + dx][y + dy] = max(dp[x + dx][y + dy], dp[x][y] + triangle[x + dx][y + dy])
            
    answer = max(dp[-1])
    return answer