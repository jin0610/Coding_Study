N = int(input())

for _ in range(N):
    closet = {}
    n = int(input())

    for _ in range(n):
        cloth, _type = input().split()
        if _type in closet:
            closet[_type].append(cloth)
        else:
            closet[_type] = [cloth]
        
    day = 1
    for key in closet:
        day *= (len(closet[key]) + 1)
    
    print(day - 1)
