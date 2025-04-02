n = input()
n_list = []
for i in n :
  n_list.append(i)

print(int(''.join(sorted(n_list, reverse=True))))