"""
모든 노드 -> 모든 노드의 최단 거리를 구하는 전형적인 플로이드 워셜 알고리즘
n = 도시 개수, m = 간선 개수

!!! 문제를 잘 읽자. 문제에 '시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.'고
명시되어있다. 그말은 a->b 로 가는 간선이 여러개일 수도 있다는 뜻이므로 graph에 값을 입력받을 때
기존에 있는 값과 새로 들어오는 c의 값을 비교하여 더 작은것으로 갱신시켜주어야 한다.!!!
"""
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

# 출발 노드와 도착 노드가 같은 경우 거리셋팅
for i in range(1, n+1) :
    graph[i][i] = 0

for i in range(m) :
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

# 플로이드 워셜 함수 시작
for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1) :
    for j in range(1, n+1) :
        if graph[i][j] == INF :
            print(0, end=' ')
        else :
            print(graph[i][j], end=' ')
    print()

