from math import *
from pylab import *
x1,y1,x2,y2=[-1.],[0.],[1.],[0.]
vx1,vy1,vx2,vy2=[0.],[-pi],[0.],[pi]
<<<<<<< HEAD
dt=0.001
=======
dt=0.002
>>>>>>> 9740be1280558073ce5ab4d96e9c283e533ab2be
t=[0]
while t[-1]<10:
    r=sqrt((x1[-1]-x2[-1])**2+(y1[-1]-y2[-1])**2)
    vx1.append(vx1[-1]+dt*(-4*pi*pi*(x1[-1]-x2[-1])/(r**3)))
    vy1.append(vy1[-1]+dt*(-4*pi*pi*(y1[-1]-y2[-1])/(r**3)))
<<<<<<< HEAD
=======
    vx2.append(vx2[-1]+dt*(-4*pi*pi*(x2[-1]-x1[-1])/(r**3)))
>>>>>>> 9740be1280558073ce5ab4d96e9c283e533ab2be
    vy2.append(vy2[-1]+dt*(-4*pi*pi*(y2[-1]-y1[-1])/(r**3)))
    x1.append(x1[-1]+vx1[-1]*dt)
    y1.append(y1[-1]+vy1[-1]*dt)
    x2.append(x2[-1]+vx2[-1]*dt)
    y2.append(y2[-1]+vy2[-1]*dt)
    t.append(t[-1]+dt)
figure(figsize=[6,6])
plot(x1,y1,'r')
plot(x2,y2,'b')
xlabel('x')
ylabel('y')
xlim(-0.1,0.1)
ylim(-1.05,-0.98)
title('two stars with same mass')
show()
show()
