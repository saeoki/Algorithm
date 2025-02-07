def solution(name, yearning, photo):
    answer = []
    sum = 0
    for i in photo :
        for photo_name in i :
            if photo_name in name :
                sum += yearning[name.index(photo_name)]
        answer.append(sum)
        sum = 0
    return answer