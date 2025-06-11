"""
일단위로 전부 카운트 한 뒤 7로 나눈 나머지가 1이면 월요일, 2면 화요일...
입력이 들어왔을 때 몇일이 더해지는지를 잘 계산만 하면 될듯
"""
month, day = map(int, input().split())
day_count = 0

for i in range(month) :
    if i in [1, 3, 5, 7, 8, 10, 12] :
        day_count += 31
    elif i in [4, 6, 9, 11] :
        day_count += 30
    elif i == 2 :
        day_count += 28

day_count += day

if day_count % 7 == 1 :
    print('MON')
elif day_count % 7 == 2 :
    print('TUE')
elif day_count % 7 == 3 :
    print('WED')
elif day_count % 7 == 4 :
    print('THU')
elif day_count % 7 == 5 :
    print('FRI')
elif day_count % 7 == 6 :
    print('SAT')
elif day_count % 7 == 0 :
    print('SUN')