a, b = map(int, input().split())
a = reversed(str(a))
b = reversed(str(b))
print(max(int(''.join(a)), int(''.join(b))))