def solution(number):
    l = len(number)
    answer = 0
    for i in range(l-2) :
        for j in range(i+1, l-1) :
            for k in range(j+1, l) :
                if number[i] + number[j] + number[k] == 0 :
                    answer += 1
    return answer

"""
`combinations`이란 모듈을 사용해서 풀이할 수도 있음
combinations은 정해진 길이의 모든 조합을 튜플 리스트 형태로 반환
예시 : result = combinations(data, 3)
[(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]

def solution (number) :
    from itertools import combinations
    cnt = 0
    for i in combinations(number,3) :
        if sum(i) == 0 :
            cnt += 1
    return cnt
"""