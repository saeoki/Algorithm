import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n) :
    OX_list = input()
    count = 0
    sum = 0
    for i in OX_list :
        if i == 'O' :
            count += 1
            sum += count
        else :
            count = 0
    print(sum)

