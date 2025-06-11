"""
A : 도시=노드, B : 버스=간선
전형적인 최단거리 알고리즘 문제, 특정 노드 -> 모든 노드의 크루스칼 알고리즘을 사용
우선순위 큐를 위해 힙을 사용
주어진 출발점 -> 도착점의 최단 거리를 출력
0. 변수 입력받기
1. 그래프, 최단 거리 테이블(INF 초기화) 만들기
2. 함수 구현
"""
def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q :
        dist, now = heapq.heappop(q)
        # 뽑은 기준 노드가 이미 처리된 것이라면 스킵
        if distance[now] < dist :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())

distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

# 그래프 입력받기
for i in range(1, m+1) :
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

start, end = map(int, input().split())

dijkstra(start)

print(distance[end])
