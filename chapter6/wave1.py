
from matplotlib import animation
from pylab import*
import numpy as np
c=300.0
dx=0.01
dt=0.01
t=0.0

y=[]
l=np.linspace(0,1,100)#x-axis
y0=np.exp(-1000*(l-0.3)**2)#y-axis it's a wave package locates at x=0.3
y0_2=np.exp(-1000*(l-0.3)**2)+np.exp(-700*(l-0.7)**2)    

def w():
    global t,dt
    y.append(y0_2)
    y.append(y0_2)
    while t<100.0:
        y_next=np.zeros(100)
       
        for i in range(1,98):
            y_next[i]=-y[-2][i]+y[-1][i+1]+y[-1][i-1]
       
        y.append(y_next)
        t=t+dt
    return y, t
#print w()[0] ,w()[1]

def w2():
    global t,dt
    y.append(y0)
    y.append(y0)
    while t<100.0:
        y_next=np.zeros(100)
       
        for i in range(1,98):
            if i<50:
                y_next[i]=-y[-2][i]+y[-1][i+1]+y[-1][i-1]
            else: 
                y_next[i]=2*(1-0.05)*y[-1][i]-y[-2][i]+0.05*(y[-1][i+1]+y[-1][i-1])
        y.append(y_next)
        t=t+dt
    return y, t
#print w()[0] ,w()[1]

a=w2()[0]
a=w2()[0]
f=figure()
ax=axes(xlim=(0,1),ylim=(-1.2,1.2))
line, =ax.plot([],[],lw=2)

def animate(i):
    line.set_data(l,a[i])
    return line,
def init():
    line.set_data([],[])
    return line,
anim=animation.FuncAnimation(f,animate,init_func=init,frames=100,interval=50,blit=True)#frames mean zhenshu,interval mean each frame last how long
show()

