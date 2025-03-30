from collections import deque
T = int(input())

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
def bfs(graph, x, y):
    q = deque()
    q.append((x, y))
    graph[y][x] = 0
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if nx >= 0 and nx < M and ny >= 0 and ny < N and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append((nx, ny))
    return graph


for i in range(T):
    M, N, K = map(int,input().split()) # M : 가로 길이, N : 세로길이
    ground = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int,input().split())
        ground[y][x] = 1

    cnt = 0
    for y in range(N):
        for x in range(M):
            if ground[y][x] == 1:
                ground = bfs(ground, x, y)
                cnt += 1

    print(cnt)