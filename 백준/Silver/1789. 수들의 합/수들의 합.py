def S_count(n) :
    sum = 0
    for i in range(1, n+1) :
        sum += i
        if(sum > n) :
            print(i-1)
            break
        elif(n == 1) :
            print(1)

S = int(input())
S_count(S)