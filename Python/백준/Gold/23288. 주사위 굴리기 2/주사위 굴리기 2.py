#전체코드# 
from collections import deque


def move_dice(direction):
    global dice
    temp = dice[:] #temp에 현재 주사위 숫자 위치를 복사
    for i in range(len(dice)):
    	# 이동 후 주사위의 숫자와 현재 주사위 숫자의 위치를 교체해준다.
        temp[i] = dice[move_map[direction][i]] 
    dice = temp[:] #다음 주사위 숫자 위치를 dice로 복사


def point_count(cx, cy, B):
    q = deque()
    check = [[False] * M for _ in range(N)]
    cnt = 0
    q.append((cy, cx))
    check[cy][cx] = True
    while q:
        y, x = q.popleft()
        cnt += 1 #같은 칸이 하나 있는 것이기 때문에 +1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #이동할 수 없거나 이미 확인된 곳이라면 넘어간다.
            if ny < 0 or nx < 0 or ny >= N or nx >= M or check[ny][nx]:
                continue
            #이동 후 현재 칸의 값과 같은 숫자라면 check해주고 q에 넣어준다.
            if Board[ny][nx] == B:
                check[ny][nx] = True
                q.append((ny, nx))
    return cnt * B


N, M, K = map(int, input().split())
Board = [list(map(int, input().split())) for _ in range(N)]
# dx, dy를 동,서,남,북 순으로 입력받을 수 있게 세팅.
dx = [1, 0, -1, 0] 
dy = [0, 1, 0, -1]
direction = 0
dice = [6, 4, 2, 3, 5, 1] #현재 주사위의 숫자(구현과정 1번 그림 참고)
# move_map = [[4, 1, 3, 6, 5, 2], [3, 2, 6, 4, 1, 5], [2, 6, 3, 1, 5, 4], [5, 2, 1, 4, 6, 3]]
move_map = [[], [], [], []]
move_map[0] = [3, 0, 2, 5, 4, 1]
move_map[1] = [4, 1, 0, 3, 5, 2]
move_map[2] = [1, 5, 2, 0, 4, 3]
move_map[3] = [2, 1, 5, 3, 0, 4]
#dx, dy가 동 서 남 북 순이기 때문에 주사위의 이동 후 숫자도 순서대로 맞춰줌
#		  0  1  2  3


current_location = (0, 0) #시작 위치
total_point = 0
for i in range(K):
	# 처음은 오른쪽으로 향하기 때문에, direction = 0 그대로 더해줌
    ny = current_location[0] + dy[direction] 
    nx = current_location[1] + dx[direction]
	# 갈 수 없는 상황일 경우, 반대로 바꿔줌
    if ny < 0 or nx < 0 or ny >= N or nx >= M:
    	#비트연산자로 반대 방향으로 바꿔준 후, ny, nx를 다시 조정
        direction = direction ^ 2
        ny = current_location[0] + dy[direction]
        nx = current_location[1] + dx[direction]
	
    current_location = (ny, nx) #현재 위치를 ny, nx로 입력
    move_dice(direction) # 주사위 숫자 변경
    B = Board[ny][nx] # 현재 칸의 숫자 값
    point = point_count(nx, ny, B)
    total_point += point
    A = dice[0] # 주사위의 아랫면
    if A > B: #주사위 아랫면이 더 클 경우 시계방향 90도
        direction = (direction + 1) % 4
    elif A < B: #주사위 아랫면이 더 작을 경우 반시계방향 90도
        direction = (direction - 1) % 4

print(total_point)