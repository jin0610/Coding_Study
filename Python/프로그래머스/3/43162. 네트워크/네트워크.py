def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def find_network(curr_com):
        nonlocal visited, computers
        
        visited[curr_com] = True
        for next_com in range(n):
            if not visited[next_com] and computers[curr_com][next_com] == 1:
                find_network(next_com)
    
    for start_com in range(n):
        if not visited[start_com]:
            find_network(start_com)
            answer += 1
    return answer