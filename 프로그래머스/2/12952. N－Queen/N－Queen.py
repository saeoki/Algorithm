def solution(n):
    answer = 0
    col = [] # col[i] = i번째 행에 놓인 퀸의 '열' 위치
    
    def is_valid(row, c) :
        for r in range(row) : # 새로 놓으려는 행의 열 위치와 지금까지 놓았던 모든 행의 열 위치를 비교
            if col[r] == c or abs(col[r] - c) == abs(r - row) : 
            # 이미 같은 열에 둔 퀸이 있거나 or 대각에 있을 때(가로 세로 거리차가 같으면 대각)
                return False
        return True
    
    def backtrack(row) :
        nonlocal answer
        if row == n:
            answer += 1
            return
        for c in range(n) :
            # 컬럼 하나 당 행끝까지 가는 탐색을 다 진행 해보는 것임
            if is_valid(row, c) :
                col.append(c) # 추가하고
                backtrack(row + 1) # 재귀 호출하고 이어지면 쭉쭉 호출하고
                col.pop() # 끝나거나 이어지지 않으면 바로 빼는 백트래킹 구조
    
    backtrack(0)
    return answer