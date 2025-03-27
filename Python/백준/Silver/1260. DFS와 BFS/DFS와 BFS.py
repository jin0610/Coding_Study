from collections import deque

N, M, V = map(int,input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

for _ in range(M):
    a, b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True

def dfs(v):
    visited_dfs[v] = True
    print(v, end=" ")
    for curr_v in range(1, N + 1):
        if not visited_dfs[curr_v] and graph[v][curr_v]:
            dfs(curr_v)

def bfs(v):
    q = deque([v])
    visited_bfs[v] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for curr_v in range(1, N+1):
            if not visited_bfs[curr_v] and graph[v][curr_v]:
                q.append(curr_v)
                visited_bfs[curr_v] = True
            

dfs(V)
print()
bfs(V)
