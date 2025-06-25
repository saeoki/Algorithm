"""
1 2 3 4 5... 순서대로 오는데 배달 순서에 맟춰 재정렬을 해야한다
스택을 사용, 스택을 써도 배달 순서에 못맞추는 상황이면 거기까지만 배달하고 종료
결과 리스트도 하나 만들어주고, 마지막에 결과 리스트의 길이를 반환하면 될 듯
"""
from collections import deque
def solution(order):
    order = deque(order)
    stack = []
    result = []
    for num in range(1, len(order)+1) :
        if num == order[0] :
            result.append(order.popleft())
        else :
            while stack and stack[-1] == order[0] :
                result.append(order.popleft())
                stack.pop()
            stack.append(num)
    
    for _ in range(len(stack)) :
        if order[0] == stack[-1] :
            result.append(order.popleft())
            stack.pop()
        else :
            break
    return len(result)
        