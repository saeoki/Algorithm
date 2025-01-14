def solution(d, budget):
    sum = 0
    result = 0
    for i in sorted(d) :
        sum += i
        if (sum <= budget) :
            result += 1
        else : 
            break
    return result