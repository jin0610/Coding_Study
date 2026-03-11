#### DFS ####
answer = 0
def dfs(curr_idx, value, numbers, target):
    global answer
    if curr_idx == len(numbers):
        if value == target:
            answer += 1
        return
    
    dfs(curr_idx + 1, value + numbers[curr_idx], numbers, target)
    dfs(curr_idx + 1, value - numbers[curr_idx], numbers, target)
        
def solution(numbers, target):
    global answer
    dfs(0, 0, numbers, target)
    return answer