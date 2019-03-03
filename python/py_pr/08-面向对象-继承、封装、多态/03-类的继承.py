class Animal:
    def eat(self):
        print("----吃-------")
    def drink(self):
        print("----喝-------")
    def sleep(self):
        print("----睡觉-------")
    def run(self):
        print("----跑-------")

#继承Animal类
class Dog(Animal):
    def bark(self):
        print("---汪汪叫--")

wangcai = Dog()
wangcai.eat()
wangcai.bark()









