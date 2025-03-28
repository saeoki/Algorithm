from collections import deque

def bfs(x, y) :
  queue = deque()
  queue.append((x, y))
  while queue :
    x, y = queue.popleft()
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >=n or ny < 0 or ny >= m :
        continue
      if graph[nx][ny] == 0 :
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  # 가장 오른쪽 최 하단 노드의 값을 리턴
  return graph[n - 1][m - 1]

n, m = map(int, input().split())

graph = []
for i in range(n) :
  graph.append(list(map(int, input())))

# 인덱스 순서대로 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))