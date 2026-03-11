visited = []
def dfs(v, n, computers):
    global visited
    
    for i in range(n):
        if computers[v][i] == 1 and not visited[i]:
            visited[i] = True
            dfs(i, n, computers)
    
def solution(n, computers):
    global visited
    visited = [False for _ in range(n)]
    answer = 0
    for i in range(n):
        if not visited[i]:
            visited[i] = True

            dfs(i, n, computers)
            answer += 1
    
    return answer