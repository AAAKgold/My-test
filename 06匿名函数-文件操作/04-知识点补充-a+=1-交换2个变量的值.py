#a = 100#不可变类型
a = [100]#可变类型

def test(num):
    num = num + num# num+=num ---->num=num+num 在Python中不是真正等价 这里赋值语句是指向  
    print(num)


test(a)
print(a)
