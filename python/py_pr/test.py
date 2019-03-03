import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return 1.0*(pow(x,4)-14*pow(x,3)+60*pow(x,2)-70*x)

def main():
    global x_opt
    global f_opt
    global stepNum
    a=0
    b=2
    l=0.3
    r=(math.sqrt(5)-1)/2
    a1=b-r*(b-a)
    a2=a+r*(b-a)
    stepNum=0
    while abs(b-a)>l:
        stepNum=stepNum+1
        f1=f(a1)
        f2=f(a2)
        if f1>f2:
            a=a1
            f1=f2
            a1=a2
            a2=a+r*(b-a)
        else:
            b=a2
            a2=a1
            f2=f1
            a1=b-r*(b-a)
        x_opt=(a+b)/2
        f_opt=f(x_opt)
    return x_opt,f_opt,stepNum

main()

x=np.linspace(0,2,100)
y=[1.0*(pow(x1,4)-14*pow(x1,3)+60*pow(x1,2)-70*x1) for x1 in x]
plt.plot(x,y)
plt.plot(x_opt,f_opt,'r*')
plt.show()
print('%.3f is the optimal point of the function and execute %d steps'%(x_opt,stepNum))



