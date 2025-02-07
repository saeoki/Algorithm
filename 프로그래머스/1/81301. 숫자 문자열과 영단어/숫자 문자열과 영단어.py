def solution(s) :
    result = ''
    check_box = ''
    number_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'}
    for i in s :
        if i in number_dict.values() :
            result += i
        else :
            check_box += i
            if check_box in number_dict.keys() :
                result += number_dict[check_box]
                check_box = ''
    return int(result)