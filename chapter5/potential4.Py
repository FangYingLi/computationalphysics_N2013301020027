#this is a program describes eletric potential between a capacitor
import numpy as np
from pylab import *

def template():
    v_init=np.zeros((7,7))
    v_init[:,0]=-1
    v_init[:,6]=1
    return v_init
# v_nit v0 means initial potential,v1 means next potential,vt means temporary potential  
dv=np.zeros((7,7))+1.

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
dx=2.0/6.
dy=2.0/6.
def func2(v0):
    dvx=np.zeros((len(v0)-1,len(v0[0])-1))#electric field,Ex
    dvy=np.zeros((len(v0)-1,len(v0[0])-1))
    for i in range(len(v0)-1):
        for j in range(len(v0[0])-1):
            dvy[i][j]=-(v0[i+1][j]-v0[i][j])/dy
            dvx[i][j]=-(v0[i][j+1]-v0[i][j])/dx
    return dvx,dvy

vt=template()
while condition(dv):# while True
    vt_next=func(vt)
    dv=vt_next-vt
    vt=vt_next
#print vt
x=np.linspace(-1+dx/2.,1-dx/2.,7-1)
y=np.linspace(-1+dx/2.,1-dx/2.,7-1)
x,y=np.meshgrid(x,y)
'''contour(x,y,vt)
colorbar()
'''
ex,ey=func2(vt)
print ex,ey
quiver(x,y,ex,ey)
xlim(-1,1)
ylim(-1,1)
xlabel('X')
ylabel('Y')
title('ELectric fleid bewteen two metal plates')
show()

