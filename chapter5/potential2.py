#this is a program describes eletric potential between a capacitor
import numpy as np
from pylab import *

def template():
    v_init=np.zeros((100,100))
    v_init[:,39]=-1
    v_init[:,60]=1
    return v_init
# v_nit v0 means initial potential,v1 means next potential,vt means temporary potential  
dv=np.zeros((100,100))+1.

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
'''
def func2(vt):
    dx=0.33
    ex=template()
    ey=template()
    for i in range(1,len(vt[0])-1):
        for j in range(len(vt[1])):
            ex[i][j]=-0.5*(vt[(i+1)%vt.shape[0]][j]+vt[i-1][j])/dx
            ey[i][j]=-0.5*(vt[i][j-1]+vt[i][(j+1)%vt.shape[1]])/dx
        return ex,ey
'''
vt=template()
while condition(dv):# while True
    vt_next=func(vt)
    dv=vt_next-vt
    vt=vt_next
print vt
x=np.linspace(-1,1.1,100)
y=np.linspace(-1,1.1,100)
z=np.linspace(0,0,100)
contour(x,y,vt)
colorbar()
'''
ex=func2(vt)[0]
ey=func2(vt)[1]
#print ex,ey
quiver(x,y,ex[1][:])
'''
xlim(-1,1)
ylim(-1,1)
xlabel('X')
ylabel('Y')
title('Equipotential lines')
show()

