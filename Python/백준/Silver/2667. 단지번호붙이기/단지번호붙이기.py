import sys
input = sys.stdin.readline

N = int(input())
# sys.stdin.readline를 할 경우 개행 문자('\n')이 들어가므로 제거해야함
apart_map = [list(map(int, list(input())[:-1])) for _ in range(N)] 

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0] # 상하좌우
# dfs 방식
def dfs(x, y):
    if x >= 0 and x < N and y >= 0 and y <= N:
        global cnt
        visited[y][x] = True
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if nx >= 0 and nx < N and ny >= 0 and ny < N and not visited[ny][nx] and apart_map[ny][nx] == 1:
                visited[ny][nx] = 1
                cnt += 1
                dfs(nx, ny)

apart_cnt = []
visited = [[False] * N for _ in range(N)]
for y in range(N):
    for x in range(N):
        if apart_map[y][x] == 1 and not visited[y][x]:
            cnt = 1
            dfs(x, y)
            apart_cnt.append(cnt)

apart_cnt.sort()
print(len(apart_cnt))
for i in range(len(apart_cnt)):
    print(apart_cnt[i])