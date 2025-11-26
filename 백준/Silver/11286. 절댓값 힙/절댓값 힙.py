"""
절댓값 대소 판별, 음수 양수 판별을 동시에 진행하는게 포인트인 문제
일단 절댓값 개념을 빼고보면 최소 수를 구하는게 요점인 문제이기에 최소 힙을 사용 O(logN)
힙에 튜플 형태로 삽입을 해서 (a, b) a 위치에는 양수버전 절대값을 삽입,
b위치에는 음수가 양수가 됐는지 양수 그자체인지를 판별하는 문자를 삽입

힙에 정수들을 양수 상태로 보관(= 절대값이 작은것이 최상단에 오게 됨)
힙에 삽입을 할 때는 x가 음수면 -붙여서 양수로 들어가고 양수면 그대로
절대값 작은것 -> 수 자체가 작은 것(음수) 우선순위
b가 -1이면 음수인데 마이너스 붙여서 양수가 된것, 0이면 양수인데 그대로 들어간 것"""
import heapq
import sys
input = sys.stdin.readline

n = int(input())
absolute_heap = []
for _ in range(n) :
    x = int(input())
    if x < 0 :
        heapq.heappush(absolute_heap, (-x, -1))
    elif x > 0 :
        heapq.heappush(absolute_heap, (x, 0))
    else :
        if absolute_heap :
            pop_x = list(heapq.heappop(absolute_heap))
            if pop_x[1] == -1 :
                pop_x[0] *= -1
            print(pop_x[0])
        else :
            print(0)

