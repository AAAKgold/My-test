def test(a,b):
    a+b


result1 = test(11,22)
print(result1)#None 因为没有return
#定义一个匿名函数
func = lambda a,b:a+b

result2 = func(11,22)
print(result2)#和普通函数不一样，不需要return
