def solution(t, p):
    result = 0
    part_str = ""
    for i in range(len(t) - len(p) + 1) : 
    # i+len(p)가 t의 길이를 초과할 수 있기 때문에 마지막점 제한 조절이 필요
    # len(p)가 3이고 t가 "3141592"일 때, 순회가 5까지만 가야 범위 초과없이 실행을 마칠 수 있음
    
        part_str = t[i:i+len(p)]
        if int(part_str) <= int(p) :
            result += 1
    return result