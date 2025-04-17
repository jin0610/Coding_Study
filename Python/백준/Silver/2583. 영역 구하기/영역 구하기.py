from collections import deque
import sys
input = sys.stdin.readline

M, N, K = map(int,input().split())
_map = [ [0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1,x2):
            _map[y][x] = 1

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
def bfs(x, y):
    q = deque()
    q.append(((x, y)))
    _map[y][x] = 1
    size = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and _map[ny][nx] == 0:
                _map[ny][nx] = 1
                size += 1
                q.append((nx, ny))
    
    return size
    
cnt = 0
location = []
for y in range(M):
    for x in range(N):
        if _map[y][x] == 0:
            size = bfs(x, y)
            location.append(size)
            cnt += 1

location.sort()
print(cnt)
print(*location)