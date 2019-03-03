class Cat:

    def __init__(self,new_name,new_age):
        self.name = new_name
        self.age = new_age

    def __str__(self):
        return "%s的年龄是%d"%(self.name,self.age)

    def eat(self):
        print("猫正在吃鱼")

    def drink(self):
        print("猫正在喝水")
    
        

tom = Cat("汤姆",12)
print(tom)
lanmao = Cat("蓝猫",5)
print(lanmao)


