n = int(input())
list_n = list(map(int, input().split()))
list_n.sort()
m = int(input())
list_m = list(map(int, input().split()))

for i in list_m :
    start = 0
    end = len(list_n)-1
    while start <= end :
        mid = (start + end) // 2
        if list_n[mid] == i :
            print(1)
            break
        elif list_n[mid] > i :
            end = mid - 1
        else :
            start = mid + 1
    else :
        print(0)
"""
이진탐색의 point는
1. 탐색 범위가 매우 크다면 탐색 속도가 가장 빠른 이진탐색을 떠올린다.
2. start와 end 값을 미리 지정해놓고, start <= end 일때까지 mid를 계속 (start+end) // 2로
지정해주며 list[mid]와 찾고자 하는 값을 비교함에 따라 start와 end를 조정해준다
3. 가장 먼저 list[mid] == 찾고자 하는 값 i 이면 return or print
   list[mid] > i 이면 end = mid - 1
   list[mid] < i 이면 start = mid + 1
"""