def solution(s):
    s = list(s)
    s.sort(reverse=1)
    return ''.join(s)