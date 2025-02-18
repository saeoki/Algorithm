T = int(input())
money_list = []
coin_arr = ""
for i in range(T) :
  money_list.append(int(input()))

for money in money_list :
  quarter_count = 0
  dime_count = 0
  nickel_count = 0
  penny_count = 0
  while money > 0 :
    if money >= 25 :
      quarter_count += money // 25
      money %= 25
    elif money >= 10 :
      dime_count += money // 10
      money %= 10
    elif money >= 5 :
      nickel_count += money // 5
      money %= 5
    else :
      penny_count += money
      money = 0
  print(f"{quarter_count} {dime_count} {nickel_count} {penny_count}")
  