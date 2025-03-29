N = int(input())
maps = [list(map(int, list(input()))) for _ in range(N)]

dx, dy = [0, 0, 1, -1], [ -1, 1, 0, 0]

def dfs(x, y):
    if x >= 0 and x < N and y >= 0 and y < N and maps[y][x] == 1:
        global cnt
        cnt += 1
        maps[y][x] = 0
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            dfs(nx, ny)
    return cnt

cnt = 0
apartment = []
for x in range(N):
    for y in range(N):
        if maps[y][x] == 1:
            count = dfs(x, y)
            apartment.append(count)
            cnt = 0 

print(len(apartment))
apartment.sort()
for i in range(len(apartment)):
    print(apartment[i])