import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import itertools

A = np.matrix([[3.0,2.0],[2.0,6.0]])
b = np.matrix([[2.0],[-8.0]])
c = 0.0

def f(x,A,b,c):
    return float(0.5*x.T*A*x-b.T*x+c)

def bowl(A,b,c):
    fig = plt.figure(figsize=(10,8))
    qf = fig.gca(projection='3d')
    size = 20
    x1 = list(np.linspace(-6,6,size))
    x2 = list(np.linspace(-6,6,size))
    x1,x2 = np.meshgrid(x1,x2)
    zs = np.zeros((size,size))
    for i in range(size):
        for j in range(size):
            x = np.matrix([[x1[i,j]],[x2[i,j]]])
            zs[i,j] = f(x,A,b,c)
    qf.plot_surface(x1,x2,zs,rstride=1,cstride=1,cmap='rainbow',linewidth=0)
    plt.show()
    return x1,x2,zs
x1,x2,zs = bowl(A,b,c)
'''
def contoursteps(x1,x2,zs,steps=None):
    fig = plt.figure(figsize = (6,6))
    cp = plt.contour(x1,x2,zs,10)
    plt.clabel(cp,inline=1,fontsize=10)
    if steps is not None:
        steps = np.matrix(steps)
        plt.plot(steps[:,0],steps[:,1],'-o')
    plt.show()
contoursteps(x1,x2,zs)

x = np.matrix([[-2.0],[-2.0]])
steps = [(-2.0,-2.0)]
i = 0
imax = 10
eps = 0.01
r = b - A*x
delta = r.T*r
delta0 =delta
while i < imax and delta > eps**2*delta0:
    alpha = float(delta/(r.T*(A*r)))
    x = x + alpha * r
    steps.append((x[0,0],x[1,0]))
    r = b - A*x
    delt = r.T*r
    i += 1
contoursteps(x1,x2,zs,steps)#有问题

Around = np.matrix([[1,0],[0,1]])
bround = np.matrix([[0],[0]])
cround = 0
x1,x2,zs = bowl(Around,bround,cround)
va = np.matrix([[2],[2]])
vb = np.matrix([[2],[-2]])
contoursteps(x1,x2,zs,[(va[0,0],va[1,0]),(vb[0,0],vb[1,0])])

x = np.matrix([[-2,0],[-2,0]])
steps = [(-2.0,-2.0)]
i = 0
imax = 10
eps = 0.01
r = bround - np.matrix([[1,0],[0,0]]) * x
delta = r.T * r
delta0 = delta
while i < imax and delta > eps**2 * delta0:
    alpha = float(delta/(r.T*(Around*r)))
    x = x + alpha * r
    steps.append((x[0,0],x[1,0]))
    r = bround - Around * x
    delta = r.T * r
    i += 1
contoursteps(x1,x2,zs,steps)#有问题

'''













