#定义了一个函数
def sum_2_nums(a,b):
    #a = 10
    #b = 20
    result = a + b
    print("%d+%d=%d"%(a,b,result))

num1 = int(input("请输入第一个数字："))
num2 = int(input("请输入第二个数字："))

#调用函数
sum_2_nums(num1,num2)
