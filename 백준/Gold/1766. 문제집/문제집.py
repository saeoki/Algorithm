"""
방향성이 있는 위상정렬 알고리즘
1. 먼주 푸는 것이 좋은 순서는 반드시 따라야함
2. 일단 쉬운 문제부터, N이 작은 것이 우선 
'우선순위'가 적용되기 때문에 단순 큐로는 구현이 힘듬
우선순위 큐(힙)을 사용해서 우선순위 로직을 적용해준다.
"""
import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

# 선후관계 그래프 입력과 진입차수 셋팅
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort() :
    result = []
    # 힙이 될 리스트 정의(힙은 그냥 리스트 만들어놓고 heapq 명령어를 사용하는 것으로 구현한다)
    p = []
    
    # 초기 그래프를 바탕으로 힙에 노드 삽입
    for i in range(1, n+1) :
        if indegree[i] == 0:
            heapq.heappush(p, i)
    # 힙이 빌때까지 반복(메인)
    while p :
        now = heapq.heappop(p)
        result.append(now)
        for next_node in graph[now] :
            indegree[next_node] -= 1
            if indegree[next_node] == 0 :
                heapq.heappush(p, next_node)

    print(*result)

topology_sort()