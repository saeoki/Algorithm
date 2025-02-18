n = int(input())
coins = [500, 100, 50, 10, 5, 1]
change = 1000 - n
count = 0

for i in coins :
  count += change // i
  change %= i

print(count)
