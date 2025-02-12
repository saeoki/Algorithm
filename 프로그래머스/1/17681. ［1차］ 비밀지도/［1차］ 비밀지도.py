def solution(n, arr1, arr2):
    added_arr = []
    
    for i in range(n) :
        added_arr.append(arr1[i] | arr2[i])
        added_arr[i] = bin(added_arr[i])[2:]

# 이진수 문자열들이 동일한 길이를 갖도록 문자열 포매팅
    for i in range(n) :
        if len(added_arr[i]) < n :
            added_arr[i] = '0' * (n - len(added_arr[i])) + added_arr[i]

        added_arr[i] = added_arr[i].replace('1', '#')
        added_arr[i] = added_arr[i].replace('0', ' ')
        
    return added_arr