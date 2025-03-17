# 14501번 : 퇴사

N = int(input())
scheduler = [list(map(int,input().split())) for _ in range(N)]

# N일을 비교하기 위해 N + 1
profits = [0 for _ in range(N + 1)]

for i in range(N-1, -1, -1):
    t, p = scheduler[i]
    # i일에 상담 했을 경우 퇴사일을 넘기면 상담하지 않음
    if i + t > N:
        profits[i] = profits[i + 1]
    else:
        # i일에 상담을 했을 경우와 안했을 경우 더 큰 값을 선택함
        profits[i] = max(profits[i + 1], p + profits[i + t])

print(profits[0])