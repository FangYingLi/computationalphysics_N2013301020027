from math import *
from pylab import *
import numpy as np
b=8.0/3

class lz:#
    def __init__(self,_r,_x=0,_y=0,_z=0,_t=0,_dt=0.0001):
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
        global b 
        while(self.t[-1]<2000):

            self.w.append(self.w[-1]-g/l*sin(self.theta[-1])*self.dt-q*self.w[-1]*self.dt+fd*sin(D*self.t[-1])*self.dt)
            self.theta.append(self.theta[-1]+self.w[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        return
    
    def plot_2d(self):
        plot(self.t,self.theta,lw=1,label=r'$ =%g$'% )
        legend(loc='best',frameon=False)
        xlim(0,)
        return

    def plot_phase(self):
        plot(self.theta,self.w,label=r'$fd=%g$'%fd)
        legend(loc='best',frameon=False)
        xlabel(r'$\theta()$')
        ylabel('w()')
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
lin=[0,0.5,1.2]#fd=lin
for i in range(len(lin)):
    a=cp(lin)
    a.cal2()
    a.plot_2d()
title(r'$ $ versus time')
xlabel('time(s)')
ylabel('r$ $()')
#show()

#theta-w phase-space plot
c=cp(0.5)
c.cal2()
figure(figsize=(12,4))
subplot(1,2,1)
c.plot_phase()

d=cp(1.2)
d.cal2()
subplot(1,2,2)
d.plot_phase()
show()

        







