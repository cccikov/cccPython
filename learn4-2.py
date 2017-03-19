temp = input('猜猜小甲鱼心里想的数: ')
guess = int(temp)
if guess == 8:
    print("哇草,你是小甲鱼心里的蛔虫吗?")
else:
    if guess > 8:
        print("哥,大了大了...")
    else:
        print("嘿,小了小了")
    n = 2
    while guess != 8 and n > 0:
        temp = input('重新猜一次: ')
        guess = int(temp)
        n -= 1
        if guess == 8:
            print("哇草,你终于才对了")
        else:
            if guess > 8:
                print("哥,大了大了...")
            else:
                print("嘿,小了小了")
print("结束了,不玩了")
