temp = input('猜猜小甲鱼心里想的数')
guess = int(temp)
if guess == 8:
    print("哇草,你是小甲鱼心里的蛔虫吗?")
    print("猜中了也没有奖励")
else:
    if guess > 8:
        print("哥,大了大了...")
    else:
        print("嘿,小了小了")
print("结束了,不玩了")
