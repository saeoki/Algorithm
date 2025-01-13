def solution(x):
    n = str(x)
    sum = 0
    answer = False
    for i in n :
        sum += int(i)
    if x % sum == 0 :
        answer = True
    return answer