import sys
input = sys.stdin.readline
n = int(input())
dict = {}
A_list = map(int, input().split())
for i in A_list :
    dict[i] = 1

m = int(input())
find_list = map(int, input().split())
for i in find_list :
    print(dict.get(i, 0))

