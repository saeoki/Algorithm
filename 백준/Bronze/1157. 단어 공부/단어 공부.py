S = input().upper()
s_list = list(set(S))
count_list = []
for i in s_list :
  count_list.append(S.count(i))

if count_list.count(max(count_list)) > 1 :
  print('?')
else :
  print(s_list[count_list.index(max(count_list))])