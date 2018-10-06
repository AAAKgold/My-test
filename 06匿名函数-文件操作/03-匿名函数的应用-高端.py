#coding=utf-8

def test(a,b,func):
    result = func(a,b)
    print(result)

func_new = input("请输入一个匿名函数：")
func_new = eval(func_new) #eval作用是把字符串的引号去掉


test(11,22,func_new)





