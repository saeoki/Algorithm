import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
dict = {}
for i in num_list :
    dict[i] = 1

m = int(input())
num_list = list(map(int, input().split()))
check_list = []
for i in num_list :
    if dict.get(i) == 1 :
        check_list.append(str(1))
    else :
        check_list.append(str(0))
print(' '.join(check_list))
