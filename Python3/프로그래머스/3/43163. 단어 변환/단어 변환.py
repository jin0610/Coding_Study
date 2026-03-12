from collections import deque

def solution(begin, target, words):
    visited = [False] * (len(words) + 1)
    
    # target이 단어목록에 없을 경우 변환할 수 없는 것으로 판단 0 return
    if target not in words:
        return 0
    
    q = deque()
    q.append([begin, 0])
    while q:
        curr, step = q.popleft()
        
        if curr == target:
            return step
        # 진행하면서 한글자씩만 다를 경우 step +1, append
        for word in words:
            count = 0
            for i in range(len(word)):
                if curr[i] != word[i]:
                    count += 1
            if count == 1:
                q.append([word, step + 1])
                
        