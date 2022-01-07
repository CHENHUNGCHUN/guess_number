import random

r = random.randint(1,100)

while True:
    number =eval(input('請輸入一個'))
    if r == number :
        print('答對')
        break
    else:
        print('猜錯囉')
        if r> number:
            print('往上猜')
        elif r<number:
            print('往下猜')