"""
idea
순회를 하며 -를 발견하면 괄호를 열고 -가 나시 나오면 그 앞에 닫는 괄호를 붙인다.
문자열이 끝나도 닫는 괄호를 붙인다.
eval() 라이브러리를 사용해서 문자열을 숫자 계산한다.
"""
s = input()
stack = []
d_string = ''
new_string = ''
for i in s :
    if i.isdigit() :
        d_string += i
    else :
        new_string += str(int(d_string))
        d_string = ''

        if i == '-' :
            if not stack :
                stack.append(i)
                new_string += '-('
            else :
                stack.pop()
                new_string += ')-('
                stack.append(i)
        elif i == '+' :
            new_string+= '+'
            
if d_string :
    new_string += str(int(d_string))
if stack :
    new_string += ')'

print(eval(new_string))