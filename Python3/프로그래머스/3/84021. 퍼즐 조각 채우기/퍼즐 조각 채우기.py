from collections import deque
    
def solution(game_board, table):
    size = len(table)
    
    def in_range(x, y):
        return 0 <= x < size and 0 <= y < size
    
    # 갯수 세기
    def bfs(x, y, grid, target):
        nonlocal visited
        
        q = deque()
        q.append((x, y))
        
        points = [(x, y)]
        dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
        while q:
            cx, cy = q.popleft()
            for dx, dy in zip(dxs, dys):
                nx, ny = cx + dx, cy + dy
                if in_range(nx, ny) and grid[ny][nx] == target and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((nx, ny))
                    points.append((nx, ny))
        return points
            
    # 퍼즐 조각 찾기
    puzzles = []
    visited = [[False] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if table[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                puzzles.append(bfs(j, i, table, 1))
                
    # 빈공간 찾기
    blanks = []
    visited = [[False] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if game_board[i][j] == 0 and not visited[i][j]:
                visited[i][j] = True
                blanks.append(bfs(j, i, game_board, 0))
    
    # 찾은 퍼즐 조각, 빈공간 좌표 정규화(최솟값을 (0,0)으로 맞추는 작업)
    def points_nomalize(points):
        points.sort()
        x_diff, y_diff = points[0]
        for i in range(len(points)):
            nx, ny = points[i]
            points[i] = (nx - x_diff, ny - y_diff)
        return points
    
    for i in range(len(puzzles)):
        puzzles[i] = points_nomalize(puzzles[i])
    
    for i in range(len(blanks)):
        blanks[i] = points_nomalize(blanks[i])
    
    def rotate(points):
        # 회전은 x, y값이 바뀐 후, y값에 -1 곱하기
        for i in range(len(points)):
            x, y = points[i][1], points[i][0] * -1
            points[i] = (x, y)
        
        points = points_nomalize(points)
        return points
            
    answer = 0
    for idx in range(len(puzzles)):
        points = puzzles[idx]
        for i in range(4):
            points = rotate(points)
            if points in blanks:
                answer += len(points)
                blanks.remove(points)
                break
            
    return answer