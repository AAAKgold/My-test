import math
import numpy as np
import matplotlib.pyplot as plt

#目标函数
def f(x):
    return pow(x,4)-14*pow(x,3)+60*pow(x,2)-70*x   

#生成一个斐波那契数列
def func(num):
    numList=[0,1]
    for i in range(num - 2):
        numList.append(numList[-2] + numList[-1])
    return numList[2:]
F=func(50) 
#print(F)#for test

#计算迭代次数 ep是很小的正实数 a,b是区间 Theta_error是精度
def getn(ep,a,b,Theta_error):
    for n in range(len(F)):
        if F[n]>=((1+2*ep)*(b-a)/Theta_error):
            return n     

#主函数        
def Fibonacci(a,b,Theta_error,ep,ep1):
    n=getn(ep,a,b,Theta_error)
    stepNum=n
    r=1-F[n-1]/F[n]#r是压缩比
    a1=a+r*(b-a)
    b1=a+(1-r)*(b-a)
    while n>=1:
        n=n-1
        f1=f(a1)
        f2=f(b1)
        if n>1:
            if f1>f2:
                a=a1
                f1=f2
                a1=b1
                r=1-F[n-1]/F[n]
                b1=a+(1-r)*(b - a)
            else:
                b=b1
                f2=f1
                b1=a1
                r=1-F[n-1]/F[n]
                a1=a+r*(b-a)
        elif n==1:
            if f1>f2:
                a=a1
                f1=f2
                a1=b1
                r=1-F[n-1]/F[n]
                b1=a+(1-(r-ep1))*(b - a)
            else:
                b=b1
                f2=f1
                b1=a1
                r=1-F[n-1]/F[n]
                a1=a+(r-ep1)*(b-a)
        else:
            if f1>f2:
                a=a1
                print(a, b)
            else:
                b=b1
    x_opt=(a+b)/2
    f_opt=f(x_opt)
    return (x_opt, f_opt,stepNum,a,b)
a=0;b=2;Theta_error=0.3;ep=0.1;ep1=0.05
x_opt,f_opt,stepNum,a,b=Fibonacci(a,b,Theta_error,ep,ep1)
#x=np.linspace(0, 2, 100)
#y=f(x)
#plt.plot(x, y)
#plt.plot(x_opt,f_opt,'r*')
print('%f是函数执行了%d后的最优点'%(x_opt,stepNum))
print('区间长度为%f'%(b-a))
#plt.show()


