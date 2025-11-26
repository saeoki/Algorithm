"""
보드를 전부 8*8 사이즈로 자르고 체스판 틀에 맞춰보면서 바꿔야 하는 값이 최소인 지점을
일일이 모두 찾는 수밖에 없음 -> 브루트포스 알고리즘
보드의 좌표 (x,y)에서 x+y가 짝수면 첫시작점(맨위맨왼)과 같은 컬러여야 하고 홀수면 다른컬러여야 함
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
ans = 64

for i in range (n-7) :
    for j in range(m-7) :
        w = b = 0
        for x in range(i, i+8) :
            for y in range(j, j+8) :
                current = board[x][y]
                # x+y가 짝수면 시작점과 같아야 함
                if (x+y) % 2 == 0 :
                    # 첫시작점이 W라는 가정
                    if current != 'W' :
                        w += 1
                    if current != 'B' :
                        b += 1
                # x+y가 홀수면 시작점과 달라야 함
                else :
                    if current != 'B' :
                        w += 1
                    if current != 'W' :
                        b += 1
        ans = min(ans, w, b)

print(ans)
