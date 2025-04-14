"""
idea
dp를 사용하여 해결하면 되는 문제
d[i] = i를 만드는 방법의 수
d[0] = 1, d[1] = 1
d[i] = d[i-3] + d[i-2] + d[i-1]
"""
t = int(input())
for i in range(t) :
    n = int(input())
    d = [0] * 12
    # 3을 만들 때 3을 쓰는것처럼 다른 수 없이 그 수 만을 사용하는 경우 (공집합도 유효한 합구성)
    d[0] = 1
    d[1] = 1
    d[2] = 2
    for j in range(3, n+1) :
        d[j] = d[j-3] + d[j-2] + d[j-1]
    print(d[n])
