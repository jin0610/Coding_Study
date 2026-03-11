#### backtracking ####
selected = []
answer = 0
def backtracking(curr_n, idx, numbers, target):
    global selected, answer
    
    if curr_n == len(numbers):
        if sum(selected) == target:
            answer += 1
        return
    
    selected.append(numbers[idx])
    backtracking(curr_n + 1, idx + 1, numbers, target)
    selected.pop()
    
    selected.append(-1 * numbers[idx])
    backtracking(curr_n + 1, idx + 1, numbers, target)
    selected.pop()
    
def solution(numbers, target):
    global answer
    backtracking(0, 0, numbers, target)
    
    return answer