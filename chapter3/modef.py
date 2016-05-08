#I found in some circumstances, use a def() to solve the whole problem is more convenient than class, so I try to use it this time

from pylab import *
from math import *
#lorentz model

def lz(r):#plot t-z, r is the variable
    x=[1]
    y=[0]
    z=[0]
    t=[0]
    dt=0.0001
    sigma=10
    b=8/3.0
    for i in range(500000):
        x.append(x[-1]+dt*sigma*(y[-1]-x[-1]))
        y.append(y[-1]+dt*(-x[-1]*z[-1]+r*x[-1]-y[-1]))
        z.append(z[-1]+dt*(x[-1]*y[-1]-b*z[-1]))
        t.append(t[-1]+dt)
    return t,z,x,y,r

'''
# z versus time at different r
figure()
subplot(3,1,1)

plot(lz(5)[0],lz(5)[1],'b',label='r=5')
xlabel('time(s)')
ylabel('z')
xlim(0,50)
ylim(0,50)
title('Lorenz model  z versus time')
legend(loc='best',frameon=False)
grid(True)

subplot(3,1,2)
plot(lz(10)[0],lz(10)[1],'g',label='r=10')
xlabel('time(s)')
ylabel('z')
xlim(0,50)
ylim(0,50)
legend(loc='best',frameon=False)
grid(True)

subplot(3,1,3)
plot(lz(25)[0],lz(25)[1],'r',label='r=25')
xlabel('time(s)')
ylabel('z')
xlim(0,50)
ylim(0,50)
legend(loc='best',frameon=False)
grid(True)
show()
'''
#phase diagram
import mpl_toolkits.mplot3d
fig=figure()
a=fig.add_subplot(111,projection='3d')
a.plot(lz(25)[2],lz(25)[3],lz(25)[1],label='r='+str(lz(25)[4]))
a.set_xlabel('x')
a.set_ylabel('y')
a.set_zlabel('z')
legend(loc='best')
show()

'''
#phase plot sectional view

def lz2(r):
    x=[1]
    y=[0]
    z=[0]
    t=[0]
    x2=[]
    y2=[]
    z2=[]
    dt=0.0001
    sigma=10
    b=8/3.0
    for i in range(700000):
        x.append(x[-1]+dt*sigma*(y[-1]-x[-1]))
        y.append(y[-1]+dt*(-x[-1]*z[-1]+r*x[-1]-y[-1]))
        z.append(z[-1]+dt*(x[-1]*y[-1]-b*z[-1]))
        t.append(t[-1]+dt)
        if t[-1]>30:#when time>30
            if abs(y[-1])<0.01:#plot sectional view, when x=0
                x2.append(x[-1])
                z2.append(z[-1])
    return x2,z2
scatter(lz2(25)[0],lz2(25)[1],s=0.5)
title('z vs x when y=0')
xlabel('x')
ylabel('z')
xlim(-10,10)
ylim(5,30)
show()

'''

