"""
'모든 정점' i에서 j, 가는 길이가 '양수'인 경로가 있는지 없는지 판별
i에서 j로 다이렉트로 갈 수도 있는것이고, 어느 지점을 거쳐서 i -> k -> j처럼 가도 되는 것
입력의 개수가 100개 내로 작으니, 플로이드 워셜 알고리즘을 사용
"""
import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            if graph[i][k] and graph[k][j] :
                graph[i][j] = 1

for row in graph :
    # * = unpacking, 리스트의 괄호를 벗겨서 출력
    print(*row)
