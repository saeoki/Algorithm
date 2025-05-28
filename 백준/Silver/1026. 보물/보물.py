"""
idea
8*0 + 7*1 + 3*1 + 2*1 + 1*6 = 7+3+2+6 = 18
결국 B는 재배열 하지 않는다 쳐도 A의 재배열로 원하는 수끼리 붙일 수 있기 때문에
그냥 최소수의 조합만 생각하면됨
반드시 B의 큰수가 A의 작은수와 곱해져야 한다는 탐욕법
"""
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = 1)
result = 0
for i in range(n) :
    result += a[i]*b[i]

print(result)