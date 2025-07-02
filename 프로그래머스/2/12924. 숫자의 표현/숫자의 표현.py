"""
'연속'하는 자연수의 합이기 때문에
절반까지만 탐색하면 됨 예를 들어 n이 100일때
50까지 갔다 치면 다음이 50,51이기 때문에 절대 불가능
49 51은 연속하는 자연수가 아님
"""
def solution(n): 
    half_n = n//2 + 1
    count = 0
    for i in range(1, half_n) :
        sum = 0
        for j in range(i, half_n+1) :
            sum += j
            if sum == n :
                count += 1
            elif sum > n :
                break
    count += 1 # 자기 자신 포함
    return count
    