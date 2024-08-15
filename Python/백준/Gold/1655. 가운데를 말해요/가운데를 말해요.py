import heapq
import sys

n = int(sys.stdin.readline())

ascHeap = []
descHeap = []
result = []
for i in range(n):
    num = int(sys.stdin.readline())

    if len(ascHeap) == len(descHeap):
        heapq.heappush(ascHeap, -num)
    else:
        heapq.heappush(descHeap, num)

    if descHeap and descHeap[0] < -ascHeap[0]:
        ascVal = heapq.heappop(ascHeap)
        descVal = heapq.heappop(descHeap)

        heapq.heappush(ascHeap, -descVal)
        heapq.heappush(descHeap, -ascVal)

    result.append(-ascHeap[0])
print(*result,sep='\n')