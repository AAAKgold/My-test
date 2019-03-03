#from sympy import * 
#import sympy
import numpy as np
import matplotlib.pyplot as plt
import math
#1. 函数 导数 
#def f(x):
#    return pow(x,4)-14*pow(x,3)+60*pow(x,2)+70*x
#dify = diff(f(x),x)
#print(dify)
#2.计算中点 比较中点处导数值

def f(x):
    return 4*pow(x,3)-42*pow(x,2)+120*pow(x,1)-70*1
def g(x):
    return pow(x,4)-14*pow(x,3)+60*pow(x,2)-70*x

def main(a0,b0,l):
    global x_opt,y_opt
    global k,f1
    k = 0
    while abs(a0-b0)>l:
        k += 1
        a1 = (a0+b0)/2
        f1 = f(a1)
        if f1 > 0:
            b0 = a1
            a1 = (a0+b0)/2
        elif f1 < 0:
            a0 = a1
            a1 = (a0+b0)/2
        else:
           x_opt = a1
    x_opt,y_opt = a1,g(a1)
    #return x_opt,y_opt,k
main(0,2,0.30)
x = np.linspace(0,2,100)
y = [g(t) for t in x]
plt.plot(x,y)
plt.plot(x_opt,y_opt,'r*')
plt.show()
print(x_opt,y_opt,k)





