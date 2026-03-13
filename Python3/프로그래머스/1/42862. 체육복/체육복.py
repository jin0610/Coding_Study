def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    
    temp = lost & reserve
    lost -= temp
    reserve -= temp
    
    for i in sorted(lost):
        if i - 1 in reserve:
            reserve.remove(i - 1)
            lost.remove(i)
        elif i + 1 in reserve:
            reserve.remove(i + 1)
            lost.remove(i)
            
    return n - len(lost)