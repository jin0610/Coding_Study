# 문제에서 제시한 정렬 연산
def sort_cal(arr):
    max_row = 0

    for i in range(len(arr)):
        temp = []
        for n in set(arr[i]):
            if n == 0:	# 0은 제외
                continue
            temp.append([n, arr[i].count(n)])
        temp = sorted(temp, key = lambda x : (x[1], x[0]))
        temp = sum(temp, [])
        arr[i] = temp[:100]	
        max_row = max(max_row, len(arr[i]))

    for i in range(len(arr)):
        if len(arr[i]) != max_row:
            arr[i] = arr[i] + [0] * (max_row - len(arr[i]))

    return arr

r, c, k = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(3)]

sec = 0 
while True:
    row, col = len(A), len(A[0])
	
    # A[r][c]가 k일 경우의 연산
    if row >= r and col >= c and A[r - 1][c - 1] == k:
        print(sec)
        break
	
    # 100초가 지났을 경우의 연산
    if sec > 100:
        print(-1)
        break    
    
    # 행의 개수 >= 열의 개수인 경우, R연산(R_cal)
    if row >= col:
        A = sort_cal(A)
    # 행의 개수 < 열의 개수인 경우, C연산(C_cal)
    else:
        A = list(zip(*A))
        A = sort_cal(A)
        A = list(zip(*A))	# 전환한 배열 되돌리기
    
    sec += 1