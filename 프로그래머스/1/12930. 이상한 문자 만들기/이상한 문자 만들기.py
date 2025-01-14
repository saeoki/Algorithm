def word_changer(word) :
    result = ''
    for i in range(len(word)) :
        if i % 2 == 0 :
            result += word[i].upper()
        else :
            result += word[i].lower()
    return result

def solution(s):
    word_list = s.split(' ') # split은 기본으로 공백을 기준으로 구분, 굳이 ' ' 안해도 됨
    for i in range(len(word_list)) :
        word_list[i] = word_changer(word_list[i])
    return ' '.join(word_list)