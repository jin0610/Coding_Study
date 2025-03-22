R,C,T = map(int,input().split())
room_map = [list(map(int,input().split())) for _ in range(R)]

dc, dr = [1, 0, -1, 0], [0, 1, 0, -1]

air = []
for r in range(R):
    if room_map[r][0] == -1:
        air.append((r, 0))

def spread(room):
    temp = [ [0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if room[r][c] != 0 and (r, c) not in air:
                direct_cnt = 0
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if  nr >= 0 and nr < R and nc >= 0 and nc < C and (nr, nc) not in air:
                        temp[nr][nc] += room[r][c] // 5
                        direct_cnt += 1
                temp[r][c] += room[r][c] - ((room[r][c] // 5) * direct_cnt)
    return temp

def air_purifier(room):
    direct = 3
    r, c = air[0][0] - 1, air[0][1]
    while True:
        nr, nc = r + dr[direct], c + dc[direct]
        if nr < 0 or nr > air[0][0] or nc < 0 or nc >= C:
            direct = (direct + 1) % 4
            nr, nc = r + dr[direct], c + dc[direct]

        if (nr, nc) == air[0]:
            room[r][c] = 0
            break

        room[r][c] = room[nr][nc]        
        r, c = nr, nc

    direct = 1
    r, c = air[1][0] + 1, air[1][1]
    while True:
        nr, nc = r + dr[direct], c + dc[direct]
        if nr < air[1][0] or nr >= R or nc < 0 or nc >= C:
            direct = (direct + 3) % 4
            nr, nc = r + dr[direct], c + dc[direct]

        if (nr, nc) == air[1]:
            room[r][c] = 0
            break

        room[r][c] = room[nr][nc]        
        r, c = nr, nc
    
    return room
time = 0
while True:
    if time == T:
        break
            
    room_map = spread(room_map)
    room_map = air_purifier(room_map)

    
    time += 1

pm = 0
for r in range(R):
    pm += sum(room_map[r])

print(pm)