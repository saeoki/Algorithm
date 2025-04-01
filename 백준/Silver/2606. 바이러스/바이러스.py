#dfs 버전
def dfs(node, visited) :
  visited[node] = True
  for next_node in graph[node] :
    if not visited[next_node] :
      dfs(next_node, visited)
  
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
result = 0

for i in range(1, m+1) :
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (n+1)
dfs(1, visited)
for count in visited :
  if count :
    result += 1

print(result - 1) # 1번 컴퓨터 제외