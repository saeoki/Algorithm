"""
큐 자료구조를 구현하는 문제
큐란 선입선출 구조 FIFO로, 파이썬에선 deque로 구현한다
"""
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()
for _ in range(N) :
    command = input().split()
    if command[0] == 'push' :
        queue.append(command[1])
    elif command[0] == 'pop' :
        if queue :
            print(queue.popleft())
        else :
            print(-1)
    elif command[0] == 'size' :
        print(len(queue))
    elif command[0] == 'empty' :
        if queue :
            print(0)
        else :
            print(1)
    elif command[0] == 'front' :
        if queue :
            print(queue[0])
        else :
            print(-1)
    elif command[0] == 'back' :
        if queue :
            print(queue[-1])
        else :
            print(-1)
