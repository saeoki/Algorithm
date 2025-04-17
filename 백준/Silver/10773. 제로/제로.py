k = int(input())
stack = []
for i in range(k) :
    checker = int(input())
    if checker == 0 :
        stack.pop()
    else :
        stack.append(checker)

print(sum(stack))