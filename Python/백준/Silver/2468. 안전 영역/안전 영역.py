import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
info = []       # 높이 정보
max_height = 0  # 가장 높은 지역의 높이
for _ in range(N):
    i = list(map(int,input().split()))
    info.append(i)
    max_height = max(max_height, max(i))

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[y][x] = True
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            # nx, ny가 영역 안에 위치하고, 방문한 적 없고, 높이가 주어진 높이보다 클 경우 방문
            if nx >= 0 and nx < N and ny >= 0 and ny < N and not visited[ny][nx] and info[ny][nx] > h:
                visited[ny][nx] = True
                q.append((nx, ny))

safe_zone = 0   # 안전 구역 수의 최댓값
for h in range(max_height + 1):
    visited = [[False] * N for _ in range(N)]   # 매 높이마다 방문 여부를 리셋해주어야 함
    zone = 0    # 안전 구역 수
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and info[i][j] > h:
                bfs(j, i)
                zone += 1
    safe_zone = max(safe_zone, zone)

print(safe_zone)