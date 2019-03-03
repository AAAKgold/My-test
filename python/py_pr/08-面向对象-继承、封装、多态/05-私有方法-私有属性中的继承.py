class A:
    def __init__(self):
        self.num1 = 100

        #私有属性
        self.__num2 = 200
    
    def test1(self):
        print("----test1---")

    #私有方法
    def __test2(self):
        print("----test2---")

    def test3(self):
        self.__test2()
        print(self.__num2)

class B(A):
    def test4(self):
        self.__test2()
        print(self.__num2)


b = B()
#b.test1()

#私有方法并不会被继承
#b.__test2()
#print(b.num1)
#私有方法不会被继承

print(b.__num2)

#b.test3()

#b.test4()





