n = int(input())    # 컴퓨터의 수
con = int(input())  # 연결되어 있는 컴퓨터 쌍의 수
com_graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(con):
    a, b = map(int,input().split())
    com_graph[a][b] = 1
    com_graph[b][a] = 1

visited = [0] * (n + 1)
def dfs(v):
    visited[v] = 1
    for curr_v in range(1, n + 1):
        if visited[curr_v] != 1 and com_graph[v][curr_v]:
            dfs(curr_v)

dfs(1)
print(sum(visited)-1)