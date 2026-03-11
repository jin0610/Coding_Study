selected = []
answer = 0
original = []
def backtracking(curr_n, idx, target):
    global selected, answer, original
    if curr_n == len(original):
        if sum(selected) == target:
            answer += 1
        return
    
    
    selected.append(original[idx])
    backtracking(curr_n + 1, idx + 1, target)
    selected.pop()

    selected.append(-1 * original[idx])
    backtracking(curr_n + 1, idx + 1, target)
    selected.pop()

def solution(numbers, target):
    global answer, original
    original = numbers.copy()
    
    backtracking(0, 0, target)
    
    return answer