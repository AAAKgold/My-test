class Game(object):


    #类属性
    num = 0


    #实例方法
    def __init__(self):
        #实例属性
        self.name = "laowang"
    
    #类方法
    @classmethod
    def add_num(cls):
        cls.num = 100



#创建对象
game = Game()



#可以通过类的名字来调用类方法
Game.add_num()
print(Game.num)


























