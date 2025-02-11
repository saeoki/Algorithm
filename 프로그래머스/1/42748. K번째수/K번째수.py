def solution(array, commands):
    answer = []
    for i in range(len(commands)) :
        comm_index = commands[i]
        arr_slice = sorted(array[comm_index[0]-1 : comm_index[1]])
        answer.append(arr_slice[comm_index[2]-1])
    return answer