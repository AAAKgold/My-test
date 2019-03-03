import numpy as np

Q = np.matrix([[3.0,0,1.0],[0.0,4.0,2.0],[1.0,2.0,3.0]])
b = np.matrix([[3.0],[0.0],[1.0]])
c = 0.0
#1.原函数
def f(x,Q,b,c):
    return float(1/2*x.T*Q*x-x.T*b+c)
#2.主函数 共轭梯度法 
def main():
    x = np.matrix([[0.0],[0.0],[0.0]])
    i = 0 #迭代次数
    #imax = 100
    eps = 0.001 #精度
    r = b - Q * x
    d = r
    deltaNew = r.T * r 
    delta0 = deltaNew
    while deltaNew > eps**2 * delta0:
        alpha = float(deltaNew/float(d.T*(Q*d)))
        x = x + alpha * d
        r = b - Q * x
        deltaOld = deltaNew
        deltaNew = r.T * r
        beta = float(deltaNew / float(d.T * Q * d))
        d = r +beta * d
        i += 1
    print(i,x,f(x,Q,b,c))
#3.调用主函数
main()                                                                               
