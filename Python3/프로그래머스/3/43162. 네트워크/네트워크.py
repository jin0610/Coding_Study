def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(v):
        visited[v] = True
        
        for next_v in range(n):
            if computers[v][next_v] == 1 and not visited[next_v]:
                dfs(next_v)
                
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)
    return answer