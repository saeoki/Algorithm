"""
특정 노드(시작점)에서 모든 노드로 가는 다익스트라 알고리즘 문제
"""
import heapq
import sys
INF = int(10**6)
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)
distance[start] = 0

for i in range(1, e+1) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start))
    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)

for i in range(1, v+1) :
    if distance[i] == INF :
        print('INF')
    else :
        print(distance[i])

