def solution(genres, plays):
    answer = []
    
    # 1. hashmap 만들기
    playDict = {} # 재생횟수
    songDict = {} # 장르별
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g in songDict:
            songDict[g] += [(i, p)]
        else:
            songDict[g] = [(i, p)]

        if g in playDict:
            playDict[g] += p
        else:
            playDict[g] = p
        
    playDict = sorted(playDict.items(), key= lambda x: x[1], reverse=True)
    for k, v in playDict:
        d = sorted(songDict[k], key=lambda x : x[1], reverse=True)
        for i, p in d[:2]:
            answer.append(i)
    return answer
