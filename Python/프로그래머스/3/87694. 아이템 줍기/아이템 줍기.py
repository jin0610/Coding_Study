from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    _max = 101
    
    for i in range(len(rectangle)):
        rectangle[i] = list(map(lambda x : 2 * x, rectangle[i]))
        
    grid = [[0] * _max for _ in range(_max)]
    for ldx, ldy, rux, ruy in rectangle:       
        for x in range(ldx, rux + 1):
            grid[ldy][x] = 1
            grid[ruy][x] = 1
            
        for y in range(ldy, ruy + 1):
            grid[y][ldx] = 1
            grid[y][rux] = 1
            
    # 좌표가 좌표를 벗어나지 않는 지 확인
    def in_range(x, y):
        return x > 0 and x < _max and y > 0 and y < _max
    
    # 좌표가 사각형 내부에 있는지 확인
    def is_inner(x, y):
        for ldx, ldy, rux, ruy in rectangle:
            if ldx < x < rux and ldy < y < ruy:
                return True
        return False
    
    # 갈 수 있는지 확인
    def can_go(x, y):
        return in_range(x, y) and grid[y][x] == 1 and not is_inner(x, y) and not visited[y][x]
    
    visited = [[False] * _max for _ in range(_max)]
    
    q = deque()
    visited[2 * characterY][2 * characterX] = True
    q.append((2 * characterX, 2 * characterY, 1))
    while q:
        cx, cy, step = q.popleft()
        
        if cx == 2 * itemX and cy == 2 * itemY:
            return step // 2
        
        # grid[cy][cx] == 1이면 직선 구간
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if can_go(nx, ny):
                visited[ny][nx] = True
                q.append((nx, ny, step + 1))