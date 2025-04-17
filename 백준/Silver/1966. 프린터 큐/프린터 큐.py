"""
idea
큐 구조를 구현한 뒤, 이제 m의 문서를 추적해야 하는데
m의 인덱스 사이클을 살펴보면, 맨 앞 문서가 제거되든, 뒤로 밀려나든 계속 -1 되다가
본인이 가장 앞 인덱스가 됐을 때 최대중요도 문서면 그냥 끝, 아니면 맨 뒤로 밀려나니까
len(queue) - 1이 된다.
"""

from collections import deque
t = int(input())
for _ in range(t) :
    n, m = map(int, input().split())
    data = deque(list(map(int, input().split())))
    count = 0

    while data :
        if data[0] < max(data) :
            data.append(data.popleft())
        else :
            count += 1
            if m == 0 :
                break            
            data.popleft()


        if m > 0 :
            m = m - 1
        else :
            m = len(data) - 1
    print(count)