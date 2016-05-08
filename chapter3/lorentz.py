from math import *
from pylab import *
import numpy as np
si=10
b=8.0/3

class lz:#the lorentz model
    def __init__(self,_r,_x=1,_y=0,_z=0,_t=0,_dt=0.0001):
        self.r=_r
        self.x=[]
        self.x.append(_x)
        self.y=[]
        self.z=[]
        self.y.append(_y)
        self.z.append(_z)
        self.t=[]
        self.t.append(_t)
        self.dt=_dt

    def cal(self):
        global si,b 
        while (self.t[-1]<1):
            self.x.append(self.x[-1]+si*(self.y[-1]-self.x[-1])*self.dt)
            self.y.append(self.y[-1]+(-self.x[-2]*self.z[-1]+self.r*self.x[-1]-self.y[-1])*self.dt)
            self.z.append(self.z[-1]+(self.x[-2]*self.y[-2]-b*self.z[-1])*self.dt)

        return
    
    def pl(self):
        plot(self.t,self.z,lw=1,label=r'$r=%g$'%self.r )
        legend(loc='best',frameon=False)
        xlim(0,20)
        return

    def plot_phase(self):
        plot(self.x,self.z,label=r'$r=%g$'%r)
        legend(loc='best',frameon=False)
        xlabel(r'$x$')
        ylabel('z')
        return
'''
    def cal2(self,fd):#limit theta in [-pi,pi]
        global g,l,D,q,x,y,f1
        while(self.t[-1]<800):
            self.w.append(self.w[-1]-g/l*sin(self.theta[-1])*self.dt-q*self.w[-1]*self.dt+fd*sin(D*self.t[-1])*self.dt)
            if self.theta[-1]>pi:
                self.theta.append(self.theta[-1]+self.w[-1]*self.dt-2*pi)
            elif self.theta[-1]<-pi:
                self.theta.append(self.theta[-1]+self.w[-1]*self.dt+2*pi)
            else :
                self.theta.append(self.theta[-1]+self.w[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        x=self.theta
        y=self.w
        f1=fd
'''
e=lz(25)
e.cal()
e.pl()
show()



'''
lin=[5,10,25]#r=lin
for i in range(len(lin)):
    a=lz(lin[i])
    a.cal()
    a.pl()
title(r'$z$ versus time')
xlabel('time(s)')
ylabel('r$z$')
show()
'''
'''
#theta-w phase-space plot
c=cp()
c.cal2(0.5)
figure(figsize=(12,4))
subplot(1,2,1)
c.plot_phase(0.5)

d=cp()
d.cal2(1.2)
subplot(1,2,2)
d.plot_phase(1.2)
show()
'''
        







