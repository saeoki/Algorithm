import sys
input = sys.stdin.readline

def checking_vps(s) :
    stack = []
    for i in s :
        if i == '(' :
            stack.append(i)
        elif i == ')' :
            if len(stack) == 0 :
                return('NO')
            else :
                stack.pop()
    if stack :
        return('NO')
    else :
        return('YES')    


t = int(input())
for _ in range(t) :
    s = input()
    print(checking_vps(s))
