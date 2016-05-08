from math import *
from pylab import *
import numpy as np

class g:#
    def __init__(self,_r,_vx,_vy=0,_x=0,_y=0,_t=0,_dt=0.002):
        self.r=_r
        self.vx=[]
        self.vx.append(_vx)
        self.vy=[]
        self.vy.append(_vy)
        self.x=[]
        self.x.append(_x)
        self.y=[]
        self.y.append(_y)
        self.t=[]
        self.t.append(_t)
        self.dt=_dt

    def cal(self):
        
        while(self.t[-1]<10):
            self.vx.append(self.vx[-1]-4*pi*pi*self.x[-1]*self.dt/self.r**3)
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.vy.append(self.vy[-1]-4*pi*pi*self.y[-1]*self.dt/self.r**3)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        return
    
    def plot_2d(self):
        plot(self.x,self.y,lw=1)
        legend(loc='best',frameon=False)
        xlabel('x(AU)')
        ylabel('y(AU)')
        return

    def cal2(self,a):
        while(self.t[-1]<20):
            self.vx.append(self.vx[-1]-4*pi*pi*self.x[-1]*self.dt*(1+a/self.r**2)/self.r**3)
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.vy.append(self.vy[-1]-4*pi*pi*self.y[-1]*self.dt*(1+a/self.r**2)/self.r**3)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)

b=g(0.47,8.2,4,0.47,0,10,0.0001)
b.cal2(0.01)
b.plot_2d()
title('Simulation of the precession of Mercury')
show()
'''
c=g(1,0,1.75*pi,1,0)
c.cal()
c.plot_2d()
title(''Earth obriting the Sun)
show()
'''
        







