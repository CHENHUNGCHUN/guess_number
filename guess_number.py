import random
range_down = eval(input('請輸入下限:'))
range_up = eval(input("請輸入上限:"))
r = random.randint(range_down,range_up)
count = 0
while True:
    count+=1
    number =eval(input('請輸入一個'))
    if r == number :
        print('猜了', count,'次答對')
        break
    else:
        if r> number:
            print('猜錯囉，往上猜')
            print('目前猜了第', count,'次')
        elif r<number:
            print('猜錯囉，往下猜')
            print('目前猜了第', count,'次')