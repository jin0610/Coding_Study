def solution(progresses, speeds):
    
    
    # 남은 일수
    days = []
    for p, s in zip(progresses, speeds):
        day = (100 - p) // s
        if (100-p) % s > 0:
            days.append(day + 1)
        else:
            days.append(day)
    
    answer = []
    front = 0
    # print(days)
    for i in range(len(days)):
        if days[i] > days[front]:
            answer.append(i - front)
            front = i
    answer.append(len(days) - front)
            
            
            
    return answer