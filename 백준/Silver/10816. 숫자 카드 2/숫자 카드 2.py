"""
입력 범위가 굉장히 크기 때문에 이진탐색류의 알고리즘을 적용해야함
M 리스트를 하나씩 순회하며 N 리스트에 몇개나 존재하는지를 확인하면 되는데
bisect_left와 bisect_right를 사용하여 범위 탐색을 하면 될 듯 하다
"""
from bisect import bisect_left, bisect_right
import sys
n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()

result_list = []
for i in m_list :
    result = str(bisect_right(n_list, i) - bisect_left(n_list, i))
    result_list.append(result)

result_list = ' '.join(result_list)
print(result_list)