class Dog(object):
    def print_self(self):
        print("大家好我是XXX，希望以后多多关照")

class Xiaotq(Dog):
    def print_self(self):
        print("hello everybody，我是你们的老大，我是123")

#函数
def introduce(temp):
    temp.print_self()
    #多态 多种表现形式 赋的值不一样 形态也不一样

dog1 = Dog()
dog2 = Xiaotq()

introduce(dog1)
introduce(dog2)


















