import sys
n = int(sys.stdin.readline())
time = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 종료 시간 오름차순, 같으면 시작 시간 오름차순
time.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

for start, end in time:
    if start >= end_time:
        count += 1
        end_time = end

print(count)