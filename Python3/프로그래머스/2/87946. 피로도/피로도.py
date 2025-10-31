from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for dungeon in permutations(dungeons, len(dungeons)):
        temp = k
        cnt = 0
        for remain_k, t in dungeon:
            if remain_k <=  temp:
                temp -= t
                cnt += 1 
            else:
                break
        answer = max(answer, cnt)
    return answer