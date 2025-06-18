"""
상하좌우를 탐색하며, 범위를 넓혀나가는 탐색문제 BFS를 통해 풀이
값이 1인 곳곳의 노드에서부터 넓혀져 나가며, 0인 노드를 만났을 때 +1
탐색, 영역확장을 끝낸 후 가장 큰 노드값이 답이됨
"""
from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 상,하,좌,우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

q = deque()
# 익은 토마토(1인 노드) 큐에 삽입
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 :
            q.append([i, j])
# 큐가 빌 때까지 bfs
while q :
    y, x = q.popleft()
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= m or ny < 0 or ny >= n or graph[ny][nx] == -1 :
            continue
        elif graph[ny][nx] == 0 :
            graph[ny][nx] = graph[y][x] + 1
            q.append([ny, nx])

day = 0
for row in graph :
    for i in row :
        if i == 0 :
            print(-1)
            exit()
    day = max(day, max(row))
# 애초에 1인 노드에서 시작을 했기때문에 날짜수로 환산하려면 -1
print(day - 1)
