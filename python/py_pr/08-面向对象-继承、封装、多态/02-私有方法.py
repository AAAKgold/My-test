'''
class Dog:
    #私有方法
    def __send_msg(self):
        print("-----正在发送短信-----")

    #公有方法
    def send_msg(self,new_money):
        if new_money>10000:
            #当验证成功后再调用上边的私有方法
            self.__send_msg()
        else:
            print("余额不足请充值后在发送短信……")

dog = Dog()
dog.send_msg(100)
'''

#del
class Dog:
    def __del__(self):
        print("------英雄over-------")

dog1 = Dog()
dog2 = dog1

del dog1 #不会调用__del__方法，因为这个对象还有其他的变量指向他，即 引用计算不是0
del dog2 #此时会调用__del__方法，因为没有变量指向他了

print("=============")

#如果在程序结束时，有些对象还存在，那么Python解释器会自动调用他们的__del__方法来完成清理工作



























