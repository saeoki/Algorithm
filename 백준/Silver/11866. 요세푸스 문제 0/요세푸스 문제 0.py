"""
1부터 N까지 이루어진 원형리스트 k번째 요소 마다 제거하고
그 제거된 요소를 리스트로 만들어서 출력하는 문제
원형 리스트여야 하기 때문에 마지막 요소 다음에 첫번 쨰 요소로 갈 수 있어야하고
삭제가 용이해야함 -> 큐(덱)을 사용 (양방향 연결리스트)
(7,3) 요세푸스순열 예시에서 3,6,2,7,5,1,4 로 3칸마다 하나씩 추출이 된다는 걸 보고 아래의 아이디어를 연상
-> k될때까지 앞에껄 빼고 뒤에 붙이고 k 됐을 때앞에걸 pop 해서 k 번쨰껄 정확히 추출
"""
from collections import deque

n, k = map(int, input().split())
circle_deque = deque(list(i for i in range(1, n+1)))
yoseputh_list = []

while circle_deque :
    for _ in range(k-1) :
        circle_deque.append(circle_deque.popleft())
    yoseputh_list.append(str(circle_deque.popleft()))

print('<', end='')
print(', '.join(yoseputh_list), end='')
print('>')