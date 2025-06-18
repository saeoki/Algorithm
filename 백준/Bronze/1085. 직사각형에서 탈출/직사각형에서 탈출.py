x, y, w, h = map(int, input().split())
down_h = y
up_h = h - y
right_w = w - x
left_w = x
print(min(down_h, up_h, right_w, left_w))