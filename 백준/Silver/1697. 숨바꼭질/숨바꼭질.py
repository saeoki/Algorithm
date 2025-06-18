"""
X에서 K까지 (x-1 or x+1 or 2*x) 3가지의 루트로 진행할 수 있고 소요시간이 1초로 모두동일
N부터 K까지의 각 숫자를 노드라고 생각하고 해당 노드까지 걸리는 최단 시간을 모두 구해주면됨
최단거리 테이블을 만들어 줌.
가중치가 없는 +1 씩의 연산의 최단거리 문제기 때문에 BFS 알고리즘을 사용한다!
"""
from collections import deque

def bfs(n, k) :
    visited = [0] * 100001
    q = deque()
    q.append(n)

    while q :
        x = q.popleft()

        if x == k :
            return(visited[x])

        for i in (x-1, x+1, x*2) :
            if 0 <= i <= 100000 and visited[i] == 0 :
                visited[i] = visited[x] + 1
                q.append(i)

n, k = map(int, input().split())
print(bfs(n, k))