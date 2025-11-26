from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque(list(i for i in range(1, n+1)))
yoseputh_list = []

while queue:
    for _ in range(k-1) :
        queue.append(queue.popleft())
    yoseputh_list.append(str(queue.popleft()))

print('<', end='')
print(', '.join(yoseputh_list), end='')
print('>')