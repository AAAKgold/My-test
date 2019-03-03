import numpy as np

A = np.matrix([[3.0,0.0],[4.0,3.0]])
b = np.matrix([[3.0],[-1.0]])
c = 0.0

def f(x,A,b,c):
    return float(0.5*x.T*A*x-b.T*x+c)

def main():
    x = np.matrix([[-0.0],[-0.0]])
    steps = [(-2.0,-2.0)]
    i = 0
    imax = 1
    eps = 0.01
    r = b - A * x
    d = r
    deltaNew = r.T * r
    delta0 = deltaNew
    while i < imax: 
    #and deltaNew > eps**2 * delta0:
        alpha = float(deltaNew/float(d.T*(A*d)))
        x = x + alpha * d
        steps.append((x[0,0],x[1,0]))
        r = b - A * x
        deltaOld = deltaNew
        deltaNew = r.T * r
        beta = float(deltaNew / float(d.T * A * d))
        d = r +beta * d
        i += 1
    print(x)
main()





















