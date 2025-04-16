from collections import deque
N = int(input())
linked_list = [[0] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    # 방향이 없는 그래프
    linked_list[a].append(b)
    linked_list[b].append(a)

parent_node = [0] * (N + 1) # 부모 노드

parent_node[1] = 0
q = deque()
q.append(1)
while q:
    node = q.popleft()
    for v in linked_list[node]:
        if parent_node[v] == 0:
            parent_node[v] = node
            q.append(v)

for i in range(2, N+1):
    print(parent_node[i])