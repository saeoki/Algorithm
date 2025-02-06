def solution(food):
    result = ''
    for i in range(1, len(food)) :
        food_div = food[i]//2
        for j in range(food_div) :
            result += str(i)
    
    reverse_result = ''.join(sorted(result, reverse=1))
    result += '0'
    result += reverse_result
    
    return result