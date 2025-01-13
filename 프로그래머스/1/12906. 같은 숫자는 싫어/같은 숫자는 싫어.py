def solution(arr):
    stack = []
    for i in arr :
        if stack and stack[-1] == i : # stack이 비어있는 경우에 인덱싱을 하면 에러가 발생
            stack.pop()
        stack.append(i)
    return stack