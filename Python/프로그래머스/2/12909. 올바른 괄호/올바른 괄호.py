def solution(s):
    answer = True
    
    arr = []
    for ss in s:
        if arr == []:
            if ss == ')':
                return False
            else:
                arr.append(ss)
        else:
            if ss == '(':
                arr.append(ss)
            else:
                arr.pop()
    
    if len(arr) > 0:
        return False
            

    return True