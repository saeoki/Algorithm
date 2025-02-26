n = input()
if len(n) == 1:
  n = '0' + n # 그리고 원래 start_num 선언을 0 붙여주기 전에 했었는데 그러면 한자리수가 들어왔을 때 next_num과 start_num이 같아질 수가 없어서 if 처리를 한번 더 해줘야함 그냥 처음부터 한자리수는 0을 달고 시작해버리면 비교하기가 훨씬 수월해진다.

start_num = n
count = 0

while True:
  count += 1
  sum_num = (int(n[0]) + int(n[1])) % 10 # 사실상 이것때문에 안된거였음
  next_num = n[1] + str(sum_num)
  n = next_num

  if next_num == start_num :
    break

print(count)