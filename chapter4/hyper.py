from math import *
import numpy as np
from pylab import *
dt=0.0001
def h():
    x=[1.]
    y=[0]
    vx=[0]
    vy=[2*pi]
    t=[0]
    the=[pi/2.0]
    w=[2*pi]
    while t[-1]<3:
        r=(x[-1]**2+y[-1]**2)**0.5
        vx.append(vx[-1]-dt*(4*pi**2*x[-1]/r**3))
        vy.append(vy[-1]-dt*(4*pi**2*y[-1]/r**3))
        x.append(x[-1]+vx[-1]*dt)
        y.append(y[-1]+vy[-1]*dt)
        w.append(w[-1]-dt*(x[-1]*sin(the)-y[-1]*cos(the))*(x[-1]*cos(the)+y[-1]*sin(the))*3*4*pi**2/r**5)
        the.append(the[-1]+dt*w[-1])
        t.append(t[-1]+dt)
    return t,the,vx,vy,x,y


plot(h()[0],h()[1])
xlabel('x(AU)')
ylabel('y(AU)')
show()
