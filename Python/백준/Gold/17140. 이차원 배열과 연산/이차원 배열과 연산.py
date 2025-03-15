# 17140번 이차원 배열과 연산

# R 연산 : 행의 개수 >= 열의 개수인 경우 적용
def R_cal(arr):
    max_row = 0

    for i in range(len(arr)):
        temp = []
        for n in set(arr[i]):
            if n == 0:
                continue
            temp.append([n, arr[i].count(n)])
        arr[i] = temp
        arr[i] = sorted(arr[i],key = lambda x : (x[1], x[0]))
        arr[i] = sum(arr[i],[])
        max_row = max(max_row, len(arr[i]))
        
    if max_row > 100:
        max_row = 100

    for i in range(len(arr)):
        if len(arr[i]) != max_row:
            arr[i] = arr[i] + [0] * (max_row - len(arr[i]))

    return arr

# C 연산 : 행의 개수 < 열의 개수인 경우 적용
def C_cal(arr):
    arr = list(zip(*arr))
    temp = []
    max_col = 0

    for i in range(len(arr)):
        temp = []
        for n in set(arr[i]):
            if n == 0:
                continue
            temp.append([n, arr[i].count(n)])
        arr[i] = temp
        arr[i] = sorted(arr[i],key = lambda x : (x[1], x[0]))
        arr[i] = sum(arr[i],[])
        max_col = max(max_col, len(arr[i]))
        
    if max_col > 100:
        max_col = 100

    for i in range(len(arr)):
        if len(arr[i]) != max_col:
            arr[i] = arr[i] + [0] * (max_col - len(arr[i]))

    arr = list(zip(*arr))
    return arr

r, c, k = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(3)]

cnt = 0
while True:
    row, col = len(A), len(A[0])

    if row >= r and col >= c and A[r - 1][c - 1] == k:
        print(cnt)
        break

    if cnt > 100:
        print(-1)
        break
    
    
    # 행의 개수 >= 열의 개수인 경우, R연산(R_cal)
    if row >= col:
        A = R_cal(A)
    # 행의 개수 < 열의 개수인 경우, C연산(C_cal)
    else:
        A = C_cal(A)
    cnt += 1
    
