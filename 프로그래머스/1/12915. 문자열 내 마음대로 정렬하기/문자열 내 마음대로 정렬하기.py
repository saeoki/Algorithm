def solution(strings, n):
    strings.sort(key = lambda x:(x[n], x)) # 다중조건 정렬, x[n] 정렬 이후 같은 x[n] 값이라면 x를 기준으로 정렬
    return strings