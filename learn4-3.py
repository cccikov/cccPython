import random
secret = random.randint(1,10)
temp = input('猜猜小甲鱼心里想的数: ')
guess = int(temp)
if guess == secret:
    print("哇草,你是小甲鱼心里的蛔虫吗?")
else:
    if guess > secret:
        print("哥,大了大了...")
    else:
        print("嘿,小了小了")
    n = 2
    while guess != secret and n > 0:
        temp = input('重新猜一次: ')
        guess = int(temp)
        n -= 1
        if guess == secret:
            print("哇草,你终于才对了")
        else:
            if guess > secret:
                print("哥,大了大了...")
            else:
                print("嘿,小了小了")
print("结束了,不玩了")
