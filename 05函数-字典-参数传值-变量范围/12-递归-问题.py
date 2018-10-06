#递归 切记 什么时候截止循环 即 if 
def test():
    print("haha")
    test()


test()#死循环 内存满了会报错
