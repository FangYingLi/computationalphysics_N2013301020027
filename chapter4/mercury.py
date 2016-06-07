from math import *
import numpy as np
from pylab import *
e=0.206
de=0.01
dt=0.0001
def m(a):
    x=[0.47]
    y=[0]
    vx=[0]
    vy=[8.2]
    t=[0]
    while t[-1]<3:
        r=(x[-1]**2+y[-1]**2)**0.5
        vx.append(vx[-1]-dt*((1+a/r**2)*4*pi**2*x[-1]/r**3))
        vy.append(vy[-1]-dt*((1+a/r**2)*4*pi**2*y[-1]/r**3))
        x.append(x[-1]+vx[-1]*dt)
        y.append(y[-1]+vy[-1]*dt)
        t.append(t[-1]+dt)
    return vx,vy,x,y


plot(m(0.1)[2],m(0.1)[3])
xlabel('x(AU)')
ylabel('y(AU)')
show()
