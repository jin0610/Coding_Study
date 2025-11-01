words = ['A', 'E', 'I', 'O', 'U']
words_comb = []
dictionary = []

def comb(cnt, w):
    global words, words_comb, dictionary
    
    if cnt == w:
        dictionary.append(''.join(words_comb))
        return
    
    for i in range(5):
        words_comb.append(words[i])
        comb(cnt + 1, w)
        words_comb.pop()
                          
    return

def solution(word):
    global words, words_comb, dictionary
    answer = 0
    
    for i in range(1, 6):
        comb(0, i)
    
    dictionary = sorted(dictionary)
    answer = dictionary.index(word) + 1
        
    

    return answer