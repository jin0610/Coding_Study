import sys
input = sys.stdin.readline

# w : 가로 길이 / h : 세로 길이
w, h = map(int,input().split())     

# 개미의 초기 위치
p, q = map(int,input().split())     

# 개미가 움직일 시간
t = int(input())               

# x 위치
if ((p + t) // w) % 2 == 0:
    p = (p + t) % w
else:
    p = w - (p + t) % w

# y 위치
if ((q + t) // h) % 2 == 0:
    q = (q + t) % h
else:
    q = h - (q + t) % h

print(p, q)