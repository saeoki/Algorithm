"""
이것도 DP문제, DP문제는 보면 딱 DP 써야겠다 감이 온다.
하나 아래 노드 기준으로 생각했을 때
max(왼쪽에서 온 놈, 오른쪽에서 온 놈)
dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
초기값 설정 대신 for 범위를 잘 지정해서 인덱스 에러를 피한다
"""
n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n) :
    for j in range(i+1) :
        if j == 0 :
            dp[i][j] += dp[i-1][j]
        elif j == i :
            dp[i][j] += dp[i-1][j-1]
        else :
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))

    