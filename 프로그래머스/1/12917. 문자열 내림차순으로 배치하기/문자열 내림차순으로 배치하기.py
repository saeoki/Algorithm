def solution(s):
    s = list(s)
    s.sort(reverse=1)
    return ''.join(s)

"""
이렇게 list로 변환 후 sort해도 되지만 sorted 메소드를 사용하면 문자열에도 정렬기능을 사용할 수 있다.
문자열을 list type으로 변환한 후 정렬을 하는 것이기에
s1 = sorted(s, reverse=1)
return ''.join(s1)
으로 전개했어도 가능했을 것
"""