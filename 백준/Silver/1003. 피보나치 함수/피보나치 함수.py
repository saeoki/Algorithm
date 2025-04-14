"""
점화식을 dp 테이블에 담는것, 초기 조건을 설정해주는 것이 가장 큰 포인트
"""
t = int(input())

zero = [0] * 41
one = [0] * 41

zero[0] = 1
zero[1] = 0
one[0] = 0
one[1] = 1

for i in range(2, 41) :
    zero[i] = zero[i-1] + zero[i-2]
    one[i] = one[i-1] + one[i-2]

for _ in range(t) :
    n = int(input())
    print(zero[n], one[n])