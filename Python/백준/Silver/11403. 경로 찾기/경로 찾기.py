import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

def dfs(v):
    for j in range(N):
        if not visited[j] and graph[v][j] == 1:
            result[i][j] = 1
            visited[j] = True
            dfs(j)

# i (0 ~ N-1)에서 갈 수있는 모든 정점(j)를 표시
result = [[0] * N for _ in range(N)]
for i in range(N):
    visited = [False] * N
    dfs(i)

for i in range(N):
    print(*result[i])