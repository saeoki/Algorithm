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