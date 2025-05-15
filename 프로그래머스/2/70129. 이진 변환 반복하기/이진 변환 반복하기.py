def solution(s):
    zero_count = 0
    count = 0
    while(s != '1') :
        new_s = ''
        for i in s :
            if i == '1' :
                new_s += i
            else :
                zero_count += 1
        
        s = bin(len(new_s))[2:]
        count += 1
    return [count, zero_count]