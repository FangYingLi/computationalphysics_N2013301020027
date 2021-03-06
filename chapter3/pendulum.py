from math import *
from pylab import *

class ps:#it means pendulum state
    def __init__(self,theta=0,w=0,t=0):
        self.w=w
        self.theta=theta
        self.t=t
g=9.8
class linp:#it means linear pendulum

    def __init__(self,ps0=ps(0,0,0),dt=0.1,length=1,step=1000):
        self.lps=[]
        self.lps.append(ps0)
        self.dt=dt
        self.length=length
        self.step=step
    def nextstate(self,now):
        global g
        nextw=now.w-(g/self.length)*now.theta*self.dt
        nexta=now.theta+nextw*self.dt
        nextt=now.t+self.dt
        return ps(nexta,nextw,nextt)
    def os(self):
        for i in range(self.step):
            self.lps.append(self.nextstate(self.lps[-1]))
        
    def trace(self):
        global x,y
        x=[]
        y=[]
        for t in self.lps:
            x.append(t.t)
            y.append(t.theta)
        plot(x,y,lw=1.5)
        ylabel('theta(rad)')
        title('Nonlinear and linear pendulum') 
        legend(('linear pendulum','nonlinear pendulum'),loc='best',frameon=False)
        xlabel('t(s)')
class nonlinp(linp):
    def nextstate(self,now):
        nextw=now.w-(g/self.length)*sin(now.theta)*self.dt
        nexta=now.theta+nextw*self.dt
        nextt=now.t+self.dt
        return ps(nexta,nextw,nextt)
a=linp(ps(15/57.3,0,0),step=800,dt=0.02)
a.os()
a.trace()

b=nonlinp(ps(15/57.3,0,0),step=800,dt=0.02)
b.os()
b.trace()
show()


