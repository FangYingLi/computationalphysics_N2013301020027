from math import *
from pylab import *
def je():
    x=[1]
    y=[0]
    vx=[0]
    vy=[2*pi]
    t=[0]
    dt=0.002
    while(t[-1]<4):
        r=sqrt(x[-1]**2+y[-1]**2)
        vx.append(vx[-1]-4*pi*pi*x[-1]*dt/r**3)
        x.append(x[-1]+vx[-1]*dt)
        vy.append(vy[-1]-4*pi*pi*y[-1]*dt/r**3)
        y.append(y[-1]+vy[-1]*dt)
        t.append(t[-1]+dt)
    return x,y
figure(figsize=[6,6])
x=je()[0]
y=je()[1]
plot(x,y,'r',lw=2)
xlabel('x(AU)')
ylabel('y(AU)')
xlim(-1,1)
ylim(-1,1)
title('Earth orbiting the Sun')
scatter([0],[0],s=2000,color='yellow')
grid(True)
show()
