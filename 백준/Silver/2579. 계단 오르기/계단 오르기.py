"""
idea
d[i] = i번째 계단에서 얻을 수 있는 최대값
하나의 계단 입장에서 받을 수 있는 이전값은 두 칸전에서 올라오는 것, 한 칸전에서 올라오는것
한 칸전에서 올라오는 것은 연속으로 3개의 계단을 밟을 수 없다는 조건 때문에 그 이전에 반드시 두 칸전에서 올라온 경우라는
제한이 붙게된다.
그중 최대값을 d[i]에 삽입한다.
이외 조건은 마지막 계단은 반드시 포함 -> 모든 칸에 대해 계산한뒤 마지막 칸 출력하면 그냥 됨,
d[i] = max(d[i-2], d[i-3] + score[i-1]) + score[i]
d[0] = 0
d[1] = score[1]
d[2] = score[1] + score[2]
"""
n = int(input())
score = [0] * 301
d = [0] * 301
for i in range(1, n+1) :
    score[i] = int(input())

d[0] = 0
d[1] = score[1]
d[2] = score[1] + score[2]

for i in range(3, n+1) :
    d[i] = max(d[i-2], d[i-3] + score[i-1]) + score[i]

print(d[n])