from matplotlib.pyplot import *
import numpy as np
from visual import *



class Planet:
    def __init__(self,_x=0,_vx=0,_y=0,_vy=0,_t=0,_dt=0.01,_beta=2):
        self.x=[]
        self.x.append(_x)
        self.t=[]
        self.t.append(_t)
        self.vx=[]
        self.vx.append(_vx)
        self.y=[]
        self.y.append(_y)
        self.vy=[]
        self.vy.append(_vy)
        self.dt=_dt
        self.beta=_beta
        #print self.theta[-1],self.t[-1],self.w[-1]
        return
    def calculate(self):
        while self.t[-1]<500:
            r=(self.x[-1]**2+self.y[-1]**2)**0.5
            self.vx.append(self.vx[-1]-4*np.pi**2*self.x[-1]/r**(self.beta+1)*self.dt)
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.vy.append(self.vy[-1]-4*np.pi**2*self.y[-1]/r**(self.beta+1)*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        return
    def plot_2d(self):
        #global x,y
        #x=self.x
        #y=self.y
        plot(self.x,self.y,label=r'$\beta=%.2f$'%self.beta)
        xlabel('x/AU')
        ylabel('y/AU')
        grid(True)
        axis('equal')
        scatter([0],[0],s=500,color='red')
        legend(loc='upper right',frameon=False)
        #title("the orbit of the planet")
        #show()
        return
#f=figure()
#subplot(221)
scene.title='planet'
scene.forward=vector(0,0.0,-0.6)
b1=Planet(1.2,0.0,0.0,2*np.pi,_beta=2.0)
b1.calculate()
b1.plot_2d()
c1=Planet(1.0,0.0,0.0,2*np.pi,_beta=2.0)
c1.calculate()
c1.plot_2d()
d1=Planet(1.1,0.0,0.0,2*np.pi,_beta=2.0)
d1.calculate()
d1.plot_2d()
e1=Planet(1.3,0.0,0.0,2*np.pi,_beta=2.0)
e1.calculate()
e1.plot_2d()
#print b1.xi
b=sphere(radius=0.1,color=color.green)
b.trail=curve(color=b.color)
c=sphere(radius=0.05,color=color.blue)
c.trail=curve(color=c.color)
d=sphere(radius=0.08,color=color.yellow)
d.trail=curve(color=d.color)
e=sphere(radius=0.2,color=color.cyan)
e.trail=curve(color=e.color)
a=sphere(pos=(0,0,0),radius=0.3,color=color.red)
for i in range(len(b1.x)):
    rate(50)
    #a.pos=(0,0,0)
    b.pos=(b1.x[i],b1.y[i],0)
    b.trail.append(pos=b.pos)
    c.pos=(c1.x[i],c1.y[i],0)
    c.trail.append(pos=c.pos)
    d.pos=(d1.x[i],d1.y[i],0)
    d.trail.append(pos=d.pos)
    e.pos=(e1.x[i],e1.y[i],0)
    e.trail.append(pos=e.pos)

'''subplot(222)
a=Planet(1.1,0.0,0.0,2*np.pi,_beta=2.5)
a.calculate()
a.plot_2d()
subplot(223)
a=Planet(1.1,0.0,0.0,2*np.pi,_beta=2.1)
a.calculate()
a.plot_2d()
subplot(224)
a=Planet(1.1,0.0,0.0,2*np.pi,_beta=2.01)
a.calculate()
a.plot_2d()
'''

show()
