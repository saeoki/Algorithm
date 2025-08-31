a = int(input())
b = int(input())
c = int(input())
n = a*b*c

n_dict = {str(i): 0 for i in range(10)}

for i in str(n):
    n_dict[i] += 1

for i in range(10) :
    print(n_dict[str(i)])