from math import *
from pylab import *
g=9.8
l=9.8
D=0.5
q=0.5

class cp:
    def __init__(self,_theta=0.2,_w=0,_t=0,_dt=pi/1000):
        self.theta=[]
        self.theta.append(_theta)
        self.t=[]
        self.t.append(_t)
        self.w=[]
        self.w.append(_w)
        self.dt=_dt
    def cal(self,fd):
        global g,l,D,q,f1
        while(self.t[-1]<2000):
            self.w.append(self.w[-1]-g/l*sin(self.theta[-1])*self.dt-q*self.w[-1]*self.dt+fd*sin(D*self.t[-1])*self.dt)
            self.theta.append(self.theta[-1]+self.w[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        
        return
    def plot_2d(self,fd):
        #print len(self.t) ,len(self.theta)
        plot(self.t,self.theta,lw=1,label=r'$fd=%g$'%fd)
        legend(loc='best',frameon=False)
        xlim(0,100)
        return

    def plot_phase(self,fd):
        plot(self.theta,self.w,label=r'$fd=%g$'%fd)
        legend(loc='best',frameon=False)
        xlabel(r'$\theta(radians)$')
        ylabel('w(radians/s)')
        return

  
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
#plot t versus theta at different fd 
'''
lin=[0,0.5,1.2]#fd=lin
for i in range(len(lin)):
    a=cp()
    a.cal2(lin[i])
    a.plot_2d(lin[i])
title(r'$\theta$ versus time')
xlabel('time(s)')
ylabel('r$\theta$(radians)')
#show()

#plot Delta_theta
aa=cp(0.2)
bb=cp(0.20001)
aa.cal(1.2)#fd=1.2
bb.cal(1.2)

d_theta=[]
for x1,x2 in zip(aa.theta,bb.theta):
    d_theta.append(abs(x1-x2))

x=[]
y=[]
for y1,y2 in zip(d_theta,aa.t):
    x.append(y2)
    y.append(y1)
plot(x,y,label=r'$fd=1.2$',color='r')
xlabel('time(s)')
ylabel(r'$\Delta\theta(radians)$')
le=legend(loc='best',frameon=False)
semilogy()
xlim(0,100)
#show()

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
#poincare section
#e=cp()
#e.cal2(0.5)
f=cp()
f.cal2(1.2)
x1=[]
y1=[]
for i in range(len(x)):
    if i%4000==1000: #equal to, not assignment
        x1.append(x[i])# pick up points and store them in empty list
        y1.append(y[i])
figure(figsize=(12,8))
subplot(2,2,1)
scatter(x1,y1,s=1.5,label=r'$fd=%g$'%f1)
legend(loc='best',frameon=False)
xlabel(r'$\theta(radians)$')
ylabel('w(radians/s)')


f=cp()
f.cal2(1.2)
x1=[]
y1=[]
for i in range(len(x)):
    if i%4000==2000: #equal to, not assignment
        x1.append(x[i])# pick up points and store them in empty list
        y1.append(y[i])
subplot(2,2,2)
scatter(x1,y1,s=1.5,label=r'$fd=%g$'%f1)
legend(loc='best',frameon=False)
xlabel(r'$\theta(radians)$')
ylabel('w(radians/s)')


f=cp()
f.cal2(1.2)
x1=[]
y1=[]
for i in range(len(x)):
    if i%4000==3000: #equal to, not assignment
        x1.append(x[i])# pick up points and store them in empty list
        y1.append(y[i])
subplot(2,2,3)
scatter(x1,y1,s=1.5,label=r'$fd=%g$'%f1)
legend(loc='best',frameon=False)
xlabel(r'$\theta(radians)$')
ylabel('w(radians/s)')

f=cp()
f.cal2(1.2)
x1=[]
y1=[]
for i in range(len(x)):
    if i%4000==0: #equal to, not assignment
        x1.append(x[i])# pick up points and store them in empty list
        y1.append(y[i])
subplot(2,2,4)
scatter(x1,y1,label=r'$fd=%g$'%f1,s=1.5)
legend(loc='best',frameon=False)
xlabel(r'$\theta(radians)$')
ylabel('w(radians/s)')

show()

        







