from itertools import permutations

def check_decimal(number):    
    if number < 2:
        return False
    
    for i in range(2, int(number ** 0.5) +1):
        if number % i == 0:
            return False
        
    return True

def solution(numbers):

    number_list = list(str(numbers))
    N = len(number_list)
    
    decimal = []
    for n in range(1, N + 1):
        for number in permutations(number_list, n):
            num = ''.join(number)
            if check_decimal(int(num)):
                decimal.append(int(num))

    answer = len(set(decimal))        
    
    return answer