def dfs(x,y) :
  if x < 0 or x >= n or y < 0 or y >= n :
    return False
  if graph[x][y] == 0 :
    return False
  elif graph[x][y] == 1 :
    graph[x][y] += number
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True
  return False
  
n = int(input())
graph = []
number = 1
for i in range(n) :
  graph.append(list(map(int, input())))

for i in range(n) :
  for j in range(n) :
    if dfs(i, j) :
      number += 1
      
print(number-1)

count_list = []
for i in range(2, number + 1) :
  flat = sum(graph, [])
  count_list.append(flat.count(i))
  
for i in sorted(count_list) :
  print(i)
