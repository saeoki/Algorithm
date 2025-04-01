from collections import deque

# dfs의 중요한 흐름은 노드에 왔으면 우선 방문 처리하고, 다음 노드로 넘어가게 재귀 호출을 하는 것
# for 문을 도는 graph[node]의 next_node보다 next_node의 재귀 호출이 먼저 되기에 깊이 탐색
def dfs(node, visited) :
  visited[node] = True
  print(node, end = ' ')
  for next_node in graph[node] :
    if not visited[next_node] :
      dfs(next_node, visited)

# bfs의 중요한 흐름 역시 노드의 방문 처리를 하고 다음 노드로 넘어갈 준비(큐에 추가)하는 것
def bfs(start, visited) :
  visited[start] = True
  queue = deque([start])

  while queue :
    node = queue.popleft()
    print(node, end=' ')
    for next_node in graph[node] :
      if not visited[next_node] :
        queue.append(next_node)
        visited[next_node] = True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m) :
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1, n+1) :
  graph[i].sort()

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

dfs(v, visited_dfs)
print()
bfs(v, visited_bfs)