"""
학생들의 키의 명확한 대소관계이기 때문에 사이클(순환성)이 없는 그래프
위상 정렬을 사용해서 그래프를 풀어준다.
1. 진입차수 테이블 초기화
2. 그래프 초기화
3. 그래프 입력 (그래프에 따른 진입차수 +1 셋팅)

"""
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort() :
    # 정렬된 노드가 들어갈 곳
    result = []
    q = deque()
    # 가장 먼저, 진입차수가 0인 노드들 큐에 삽입
    for i in range(1, n+1) :
        if indegree[i] == 0 :
            q.append(i)
    # 큐가 빌 때까지 위상 정렬
    while q :
        now = q.popleft()
        result.append(now)

        for i in graph[now] :
            indegree[i] -= 1
            if indegree[i] == 0 :
                q.append(i)
    print(*result)

topology_sort()