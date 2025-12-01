"""
N개의 로프가 주어지고 이 로프들을 병렬 연결해서 들 수 있는 최대의 중량을 구하기
로프를 많이 연결한다고 좋은 것은 아님. 값이 유난히 작은 변수가 있으면 다른 큰 값을 못이겨냄
너무 작은 로프는 안쓰는게 나음
- (최소값 * 로프 갯수)
- 최대값
비교해서 후자가 더 크면 맨 앞의 가장 작은 로프를 제거

test case)
5
5
10
20
45
50
"""
from collections import deque
n = int(input())
n_list = []
for _ in range(n) :
    n_list.append(int(input()))

n_list = deque(sorted(n_list))
max = n_list[-1]
for _ in range(n) :
    parallel = n_list[0] * len(n_list)
    if parallel > max :
        max = parallel
    n_list.popleft()


print(max)
