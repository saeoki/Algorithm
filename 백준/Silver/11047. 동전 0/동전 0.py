n, k = map(int, input().split())
coin_list = []
count = 0
for _ in range(n) :
  coin_list.append(int(input()))
coin_list.sort(reverse=True)

for coin in coin_list :
  if coin > k :
    continue
  count += k // coin
  k %= coin

print(count)
