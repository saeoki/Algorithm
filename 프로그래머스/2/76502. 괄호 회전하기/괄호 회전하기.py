"""
덱을 사용해서 회전을 구현, s의 길이만큼 반복하며 회전
회전할때마다 올바른 괄호문자열인지 검증
기존 s에 대해서도 검증해야 하기 때문에 검증 -> 회전으로 구현
"""
from collections import deque

def solution(s):
    q = deque(s)
    count = 0
    for _ in range(len(s)) :
        stack = []
        flag = True
        for i in q :
            if i == '(' or i == '{' or i == '[' :
                stack.append(i)
            else :
                if stack :
                    if stack[-1] == '(' and i == ')' :
                        stack.pop()
                    elif stack[-1] == '{' and i == '}' :
                        stack.pop()
                    elif stack[-1] == '[' and i == ']' :
                        stack.pop()
                else :
                    flag = False
        if flag and not stack :
            count += 1
        q.append(q.popleft())
    return count
        
        