def solution(sizes):
    x_max = 0
    y_max = 0
    for size in sizes :
        size.sort(reverse = True)
        if size[0] > x_max :
            x_max = size[0]
        if size[1] > y_max :
            y_max = size[1]
            
    return x_max * y_max