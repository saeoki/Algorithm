from collections import deque

def bfs() :
  queue = deque()
  queue.append([0,0])
  while queue :
    node = queue.popleft()
    x, y = node[0], node[1]
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m :
        continue
      if graph[nx][ny] == 0 :
        continue
      elif graph[nx][ny] == 1:
        graph[nx][ny] += graph[x][y]
        queue.append([nx, ny])
  print(graph[n-1][m-1])

n, m = map(int, input().split())
graph = []
for i in range(n) :
  graph.append(list(map(int, input())))

# 인덱스 순서대로 상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
bfs()