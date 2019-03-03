import math
from sympy import*

#1. 原函数 导函数 二阶导
i = symbols("i")
def f(i):
    return -300+96*(pow(1+i,5)-1)/(i*(pow(1+i,5)))

def g(i):#一阶导
    #return diff(f(i),i)#求导函数
    return 480/(i*(i + 1)) - 5*(96*(i + 1)**5 - 96)/(i*(i + 1)**6) - (96*(i + 1)**5 - 96)/(i**2*(i + 1)**5)
#print(g(i).subs('i',0.1))#for test

#2. 一维牛顿法迭代
def main(i,e):#i是初值,e是精度
    k = 0
    while abs(f(i)/g(i))>e:
        i -= f(i)/g(i)
        k += 1
    print(k,i,f(i))

#3.调用主函数

main(0.10,0.0001)                                                                                                           
