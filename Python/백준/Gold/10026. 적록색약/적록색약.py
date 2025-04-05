import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 배열 범위 내, 색깔 같고, 방문 안한 경우
            if 0 <= nx < n and 0 <= ny < n and graph[x][y] == graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1  # 방문 처리
                q.append((nx, ny))


n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
ans = [0, 0]
# 정상인이 볼 때의 그룹 개수
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            ans[0] += 1
# 적록색맹이 볼 때의 그룹 개수를 새기 위하여 초록색을 빨간색으로 바꿈
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
# 적록색맹인이 볼 때의 그룹 개수
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            ans[1] += 1
# 출력
print(' '.join(map(str, ans)))