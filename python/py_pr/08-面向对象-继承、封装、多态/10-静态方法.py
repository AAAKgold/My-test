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

    #静态方法
    @staticmethod
    def print_menu():
        print("----------------------")
        print("  刺激战场V01.1")
        print("  1. Start")
        print("  2. Gameover")
        print("----------------------")

#创建对象
game = Game()

'''
#可以通过类的名字来调用类方法
Game.add_num()
print(Game.num)

#通过类 去调用静态方法
Game.print_menu()
'''

#还可以通过对象调用
game.add_num()
print(Game.num) #why

game.print_menu()







