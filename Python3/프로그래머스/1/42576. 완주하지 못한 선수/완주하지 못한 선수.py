def solution(participant, completion):
    answer = ''
    hashDict = {}
    sumHash = 0
    
    for p in participant:
        hashDict[hash(p)] = p  # hash 인덱스 넣기
        sumHash += hash(p) # hash 총합
    
    for c in completion:
        sumHash -= hash(c)
        
    return hashDict[sumHash]