n = int(input())
n_list = []
total = 0
# 입력을 모두 한 줄 안에, 공백을 기준으로 넣을 때
n_list = list(map(int, input().split()))
sorted_n_list = sorted(n_list)
for i in range(len(sorted_n_list)) :
  # sum 함수와 sum 이라는 변수명을 같이 쓰면 에러발생 변수명 주의
  total += sum(sorted_n_list[0:i+1])

print(total)