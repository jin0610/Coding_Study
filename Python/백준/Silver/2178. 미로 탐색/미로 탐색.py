from collections import deque

N, M = map(int,input().split())
Map = [list(map(int,list(input()))) for _ in range(N)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M and Map[nx][ny] == 1:
            q.append((nx, ny))
            Map[nx][ny] = Map[x][y] + 1

print(Map[N-1][M-1])