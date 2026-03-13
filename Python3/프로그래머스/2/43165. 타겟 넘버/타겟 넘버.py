def solution(numbers, target):
    answer = 0
    
    def dfs(curr, cnt, number):
        nonlocal answer
        
        if cnt == len(numbers):
            if number == target:
                answer += 1
            return
        
        dfs(curr + 1, cnt + 1, number + numbers[curr])
        dfs(curr + 1, cnt + 1, number - numbers[curr])
    
    dfs(0, 0, 0)
    return answer