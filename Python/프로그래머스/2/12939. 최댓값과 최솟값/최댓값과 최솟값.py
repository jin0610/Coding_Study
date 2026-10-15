def solution(s):
    answer = ''
    
    split_string = s.split(" ")
    string_to_int = list(map(int, split_string))
    
    _max, _min = max(string_to_int), min(string_to_int)
    
    answer = str(_min) + " " + str(_max)
    return answer