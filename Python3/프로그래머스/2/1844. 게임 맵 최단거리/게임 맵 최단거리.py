from collections import deque

N, M = 0, 0

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M
    
def solution(maps):
    global N, M, MAPS
#     격자의 크기 구하기
    N, M = len(maps), len(maps[0])
    
    visited = [[False for _ in range(M)] for _ in range(N)] # 방문여부 배열 초기화
    distance = [[ N * M for _ in range(M)] for _ in range(N)] # 거리 표시
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1] # 상하좌우 방향 설정
    
    q = deque([(0, 0)])
    visited[0][0] = True

    distance[0][0] = 1
    while q:
        cx, cy = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if in_range(nx, ny) and not visited[nx][ny] and maps[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = True

                distance[nx][ny] = min(distance[nx][ny], distance[cx][cy] + 1)
                
                
    
    if visited[N-1][M-1]:
        answer = distance[N-1][M-1]
    else:
        answer = -1
        
    return answer