from collections import deque

wheel = [deque(list(map(int,list(input())))) for _ in range(4)]
K = int(input())

# 오른쪽 방향의 톱니바퀴 살펴보기
def isRotateRight(w, d):  
    if w > 3:
        return 

    if wheel[w][6] != wheel[w -1][2]:
        isRotateRight(w + 1, -d)
        wheel[w].rotate(d)

# 왼쪽 방향의 톱니바퀴 살펴보기
def isRotateLeft(w, d):
    if w < 0:
        return 

    if wheel[w][2] != wheel[w + 1][6]:
        isRotateLeft(w - 1, -d)
        wheel[w].rotate(d)

# k번 움직이며 톱니바퀴 위치 구하기
for _ in range(K): 
    num, direct = map(int,input().split())
    num -= 1
    isRotateRight(num + 1, -direct)
    isRotateLeft(num - 1, -direct)

    wheel[num].rotate(direct)

# 점수 구하기
score = 0
for i in range(4):
    score += (wheel[i][0]) * (2 ** i)

print(score)