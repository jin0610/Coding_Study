import math

T = int(input())
test_cases = [list(map(int, input().split(' '))) for _ in range(T)]

result = []

for case in test_cases:
    x1, y1, r1, x2, y2, r2 = case

    # 조규현과 백승현의 거리 구하기
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    # 두 원이 동심원이고 반지름이 같을 때 -> 조규현과 백승현의 위치가 같을 때
    if distance == 0 and r1 == r2: 
        print(-1)
    # 내접, 외접일 때
    elif distance == abs(r2-r1) or (r1 + r2) == distance:
        print(1)
    # 두 원이 서로다른 두 점에서 만날때
    elif  abs(r2-r1) < distance < (r1 + r2):
        print(2)
    else:
        print(0)