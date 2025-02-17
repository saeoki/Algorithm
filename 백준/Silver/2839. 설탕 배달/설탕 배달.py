N = int(input())
count = 0

while N >= 0 :
  if N % 5 == 0 :
    count += N//5
    print(count)
    break
  N -= 3
  count += 1
else :
  print(-1)

"""
일단 5로 나누는 경우가 가장 탐욕적, 5로 나누어 떨어지지 않으면 3을 사용
5로 나누어 떨어질때까지 (= 5를 최대한 많이 사용하는 케이스) 3키로를 쓰며 (무게에서 3을 빼며) 최적의 해를 유도
while-else문으로 while 내에서 break가 안되었을 경우(= while 조건을 이탈했을 경우) 예외 처리를 해줌
"""