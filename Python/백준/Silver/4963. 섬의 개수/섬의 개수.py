import sys
from collections import deque
input = sys.stdin.readline

# 북, 북동, 동, 동남, 남, 남서, 서, 북서
dx, dy = [0, 1, 1, 1, 0, -1, -1, -1],[-1, -1, 0, 1, 1, 1, 0, -1]
def bfs(x, y):
    _map[y][x] = 0
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for d in range(8):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < w and 0 <= ny < h and _map[ny][nx] == 1:
                _map[ny][nx] = 0
                q.append((nx, ny))
    
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    _map = [list(map(int,input().split())) for _ in range(h)]
    land = 0
    for y in range(h):
        for x in range(w):
            if _map[y][x] == 1:
                bfs(x, y)
                land += 1
    print(land)