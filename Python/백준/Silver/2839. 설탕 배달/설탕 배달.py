import sys
N = int(input())

total = sys.maxsize
is_N = False
for i in range(N // 5, -1, -1):
    re = N - (i * 5)
    if re % 3 != 0:
        continue
    total = min(total, i + (re // 3))
    is_N = True

if not is_N:
    print(-1)
else:
    print(total)