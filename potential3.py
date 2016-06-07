#this is a program describes eletric potential between a capacitor
import numpy as np
from pylab import *

dx=(1.-(-1.))/(10.)
dy=(1.-(-1.))/(10.)

def template():
    v_init=np.zeros((100,100))
    v_init[40:60,40]=-1
    v_init[40:60,60]=1
    return v_init
# v_nit v0 means initial potential,v1 means next potential,vt means temporary potential  
dv=np.zeros((7,7))+1.

def tem2(v_2):
    v_2[40:60,40]=-1
    v_2[40:60,60]=1
    return v_2

def condition(dv):
    if np.all(dv<1e-5):
        return False #end iteration
    return True

def func(v0):
    v1=template()
    for i in range(v0.shape[0]):
        for j in range(1,v0.shape[1]-1):#first column and last column don't ivolve in iteration
            v1[i][j]=0.25*(v0[(i-1)%v0.shape[0]][j]+v0[(i+1)%v0.shape[0]][j]+v0[i][j-1]+v0[i][j+1])# predictory boundary for i to aviod index flow
    return v1

def func2(v0):
    dvx=np.zeros((len(v0)-1,len(v0[0])-1))
    dvy=np.zeros((len(v0)-1,len(v0[0])-1))
    for i in range(len(v0)-1):
        for j in range(len(v0[0])-1):
            dvx[i][j]=-(v0[i][j+1]-v0[i][j])/dx
            dvy[i][j]=-(v0[i+1][j]-v0[i][j])/dy
    return dvx,dvy

vt=template()
while condition(dv):# while True
    vt_next=func(vt)
    vt_next2=tem2(vt_next)
    dv=vt_next2-tem2(vt)
    vt=vt_next2

print(vt)

x=np.linspace(-1./10*25,1./10*25,100)
y=np.linspace(-1./10*25,1./10*25,100)
x,y = np.meshgrid(x,y)
#z=np.linspace(0,0,7)
contour(x,y,vt)
colorbar()
'''
ex,ey = func2(vt)
#print ex,ey
quiver(x,y,ex, ey)
'''
xlim(-1,1)
ylim(-1,1)
xlabel('X')
ylabel('Y')
#title('Electric field near two metal plates')
title('Equipotential lines')
show()


