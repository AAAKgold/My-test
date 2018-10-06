import random

#1.提示并获取用户输入
player = int(input("请输入 0剪刀 1石头 2布"))

#2.让电脑出一个
#computer =自动出一个 
computer = random.randint(0,2)



#2.判断用户输入，然后显示对应结果
#if 玩家获胜条件:
if (player==0 and computer==2) or (player==1 and computer==0) or (player==2 and computer==1):
    print("赢了，")
elif player==computer:
    print("平局")
else:
    print("输了，")
