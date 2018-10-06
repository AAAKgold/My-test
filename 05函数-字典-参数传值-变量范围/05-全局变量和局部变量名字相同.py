a = 100

#建议
g_a = 100

def test():
    a = 200#函数里面局部变量为主 +global就是修改全局变量
    print("a=%d"%a)

def test2():
    print("a=%d"%a)

test()
test2()
