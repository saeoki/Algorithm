def solution(arr):
    stack = []
    for i in arr :
        if stack and stack[-1] == i : # stack이 비어있는 경우에 인덱싱을 하면 에러가 발생
            stack.pop() # 대신 continue로 그냥 append 자체를 생략 시켜버릴수도 있겠음
        stack.append(i)
    return stack