#输入公交卡余额
cardBalance_s = input("请输入公交卡当前余额：")
cardBalance = int(cardBalance_s)

#输入空座位数量
emptySeat_s = input("请输入当前公交车空座位数量")
emptySeat =int(emptySeat_s)


#判断公交卡余额超过2元就可以上公交车
if cardBalance>2:
    print("余额充足，可以上公交车")

#判断能否坐下
    if emptySeat>0:
        print("车上有空座位，可以坐下")
    else:
        print("车上没有空座位，只能站着")


else:
    print("卡里余额不足，无法乘车")


