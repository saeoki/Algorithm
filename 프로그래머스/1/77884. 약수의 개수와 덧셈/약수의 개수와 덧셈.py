def divisor(n) :
    divisor_arr = []
    for i in range(1, n+1) :
        if n % i == 0 :
            divisor_arr.append(i)
    return len(divisor_arr)

def solution(left, right):
    sum = 0
    for i in range(left, right + 1) :
        div_count = divisor(i)
        if div_count % 2 == 0 :
            sum += i
        else :
            sum -= i
    return sum