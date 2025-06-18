"""
트리 형태를 띄며, 아래 노드들을 조합하여 상위 노드를 만들 수 있는 전형적인 DP 문제
큰 문제를 작은 문제로 나눌 수 있으며, 작은 문제에서 구한 정답이 큰 문제에서도 사용됨
점화식 : D[k][n] = D[k-1][1] + D[k-1][2] + .. + D[k-1][n]
D[0][i] = i
"""
t = int(input())
for _ in range(t) :
    k = int(input())
    n = int(input())
    dp = [[0] * (n+1) for _ in range(k+1)]
    
    # 0층 테이블 초기화
    for i in range(1, n+1) :
        dp[0][i] = i

    for i in range(1, k+1) :
        for j in range(1, n+1) :
            if dp[i][j] == 0 :
                for l in range(1, j+1) :
                    dp[i][j] += dp[i-1][l]

    print(dp[k][n])
