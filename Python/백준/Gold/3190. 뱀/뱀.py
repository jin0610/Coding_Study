from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
apples = [list(map(int,input().split())) for _ in range(K)]

L = int(input())
info = [list(input().split()) for _ in range(L)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1] # 우, 하, 좌, 상
snake = deque([(0, 0)])
direct = 0
x, y = 0, 0
sec = 0

while True:
    sec += 1
    nx, ny = x + dx[direct], y + dy[direct]
    
    if nx < 0 or nx >= N or ny < 0 or ny >= N or (nx, ny) in snake:
        break
    
    snake.append((nx, ny))
    if [ny + 1, nx + 1] in apples:
        apples.remove([ny + 1, nx + 1])
    
    else:
        snake.popleft()
    x, y = nx, ny

    if len(info) > 0 and sec == int(info[0][0]):
        if info[0][1] == "L":
            direct = abs(direct + 3) % 4
        else:
            direct = (direct + 1) % 4
        del info[0]

print(sec)    