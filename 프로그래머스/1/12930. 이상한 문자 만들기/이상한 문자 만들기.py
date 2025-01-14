def word_changer(word) :
    result = ''
    for i in range(len(word)) :
        if i % 2 == 0 :
            result += word[i].upper()
        else :
            result += word[i].lower()
    return result

def solution(s):
    word_list = s.split(' ')
    # split은 기본으로 공백을 기준으로 구분하지만 연속된 공백도 하나의 공백으로 간주해버리기 때문에
    # 정확히 공백 하나로 구분하는 것을 원한다면 이처럼 지정해줘야함
    for i in range(len(word_list)) :
        word_list[i] = word_changer(word_list[i])
    return ' '.join(word_list)