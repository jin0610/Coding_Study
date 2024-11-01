def solution(clothes):
    
    # 1. hash 만들기
    hashDict = {}
    
    for name, _type in clothes:
        if _type in hashDict:
            hashDict[_type] += [name]
        else:
            hashDict[_type] = [name]
        
    # A종류 n개 B종류 m개 사용한 모든 경우의 수(아무것도 착용하지 않는 경우 제외) : (n+1)(m+1) - 1 
    answer = 1
    for key, value in hashDict.items():
        answer *= (len(value) + 1)
    
    return answer - 1