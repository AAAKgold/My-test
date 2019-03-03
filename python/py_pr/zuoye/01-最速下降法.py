import numpy as np
import sympy
import matplotlib.pyplot as plt
import tkinter
def secant_search(f,d,x):
    def Alpha(alpha):
        return f(x+alpha*d)
    def Alpha_d(a):
        alpha=sympy.Symbol('alpha',real=True)
        return sympy.diff(f(x+alpha*d),alpha,1).doit().subs(alpha,a)
    def Secant(a):
        a0,a1 = a
        stepNum = 0
        a2 = a1 - (a1 - a0) / (Alpha_d(a1) - Alpha_d(a0)) *Alpha_d(a1)
        while abs(a2 - a1) > 10**(-5):
            stepNum = stepNum + 1
            a0 = a1
            a1 = a2
            a2 = a1 - (a1 - a0) / (Alpha_d(a1) - Alpha_d(a0)) * Alpha_d(a1)
        return (a2)
    a=[0.3,0.2]
    alpha= Secant(a)
    return alpha




    

import numpy as np
import matplotlib.pyplot as plt
import random
import secant_search
#from secant_search import  secant_search
#from mpl_toolkits.mplot3d import axes3d
#from matplotlib import cm
#from mpl_toolkits.mplot3d import Axes3D as ax3

def F(x):
    return (x[0]-4)**4+(x[1]-3)**2+4*(x[2]+5)**4

def g(x):
    return np.array([4*(x[0]-4)**3,2*(x[1]-3),16*(x[2]+5)**3])

def steepest(x0):
    print('初始点为:')
    print(x0,'\n')
    imax =10
    W=np.zeros((3,imax))
    W_d=np.zeros((3,imax))
    W[:,0] = x0
    i = 1
    x = x0
    grad = g(x)
    W_d[:,0] = grad
    delta = sum(grad**2)  # 初始误差
    while i<imax and delta>10**(-5):
        p=-g(x)
        x0=x
        alpha=secant_search(F,p,x)
        print(alpha)
        x=x+alpha*p
        print(x)
        W[:,i]=x
        grad=g(x)
        W_d[:, i]=grad
        print(grad)
        delta=sum(grad**2)
        i=i+1
    print("迭代次数为:",i-1)
    print("近似最优解为:")
    print(x,'\n')
    W=W[:,0:i]  # 记录迭代点
    W_d= W_d[:, 0:i]  #记录迭代梯度
    return W,W_d

x0 = np.array([4,2,-1])
W,W_d=steepest(x0)
print(W)
print(W_d)

#ax3=plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
#ax3.plot3D(W[0,:],W[1,:],W[2,:],'ro--')
#ax3.set_zlabel('z')  # 坐标轴
#ax3.set_ylabel('y')
#ax3.set_xlabel('x')
#plt.show()
