def solution(s) :
    answer = []
    dict = {}
    for i, char in enumerate(s) : # 문자열의 인덱스와 문자를 동시에 순회
        if char in dict :
            answer.append(i - dict[char])
        else :
            answer.append(-1)
        dict[char] = i
    return answer