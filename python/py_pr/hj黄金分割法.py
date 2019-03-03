#黄金分割法确定单峰函数在区间的极小点
import numpy as np
import matplotlib.pyplot as plt
import math

#定义目标函数
def func(x):
    return pow(x,4)-14*pow(x,3)+60*pow(x,2)-70*x
#print(func(1)) #for test

#def func(x):
#    return pow(x,3)-2*x+1

#定义主函数 黄金分割法计算
def main(a0,b0,l):#区间和精度
    global x_opt 
    global f_opt  
    global k
    #初值区间[0,2] l为精度 注意：1-r为压缩比
    r = (math.sqrt(5)-1)/2
    k = 0
    a1 = a0+(1-r)*(b0-a0)
    b1 = a0+r*(b0-a0)
    #循环分割 if判断
    while abs(b0-a0) > l:
        k += 1
        f1 = func(a1)
        f2 = func(b1)
        if f1 >= f2:
            a0 = a1
            a1 = b1
            f1 = f2
            b1 = a0+r*(b0-a0)
        else:
            b0 = b1
            b1 = a1
            f2 = f1
            a1 = a0+(1-r)*(b0-a0)
        x_opt = (a0+b0)/2
        f_opt = func(x_opt)
    return (x_opt,f_opt,k)
    #print(a0,b0)#for test



main(0,2,0.3)
#main(0,3,0.15)



#x = np.linspace(0,2,100)
#y = [func(t) for t in x]
#plt.plot(x,y)
#plt.show()

print("%.5f is the optimal point of the function and execute %d steps and the answer is %.5f"%(x_opt,k,f_opt))



