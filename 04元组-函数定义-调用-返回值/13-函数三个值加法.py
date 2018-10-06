def sum_3_nums(a,b,c):#形参
    result = a+b+c
    #print("%d+%d+%d=%d"%(a,b,c,result))
    return result#存储到result


def average_3_nums(a1,a2,a3):#接受的叫形参
    result = sum_3_nums(a1,a2,a3)#实参
    result = result/3
    #print("平均值是%d"%result)
    return result

def pf_3_nums(a,b,c):
    result = average_3_nums(a,b,c)*average_3_nums(a,b,c)
    print("平均值的平方是%d"%result)


#1.获取三个数值
num1 = int(input("第一个值："))
num2 = int(input("第二个值："))
num3 = int(input("第三个值："))



#sum_3_nums(num1,num2,num3)
#average_3_nums(num1,num2,num3)#传的叫实参
pf_3_nums(num1,num2,num3)





