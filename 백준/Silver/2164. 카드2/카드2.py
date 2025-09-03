"""
리스트의 제일 앞과 제일 끝을 처리하는 자료구조가 필요
제일 앞의 요소를 버리고, 또 제일 앞의 요소를 빼서 제일 뒤의 요소에 삽입
deque 라이브러리
"""
from collections import deque
n = int(input())
q = deque(range(1,n+1))
while len(q) > 1 :
    q.popleft()
    q.append(q.popleft())
print(q[0])
