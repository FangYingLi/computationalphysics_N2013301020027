#This is a program about power spectrum of a string wave by lifangying
from matplotlib import animation
from pylab import*
import numpy as np
c=300.0
dx=0.01
dt=dx/c
length=1
l=np.linspace(0,length,int(length/dx)+1)
init=np.exp(-1000*(l-0.5)**2)
init[1]=init[-2]=0.

def iterator(tfinal,dt,init,update_rule):
    result=[init,init]#result is a big list with many sublist
    t=0.0
    
    while t<tfinal:
        result.append(update_rule(result[-2:],dt))
        t+=dt
    del result[0]
    return result

def update_rule(current,dt):
    #current array is a big list with many sublist,each sublist's length is total length-2
    #constant used in equation
    r=c*dt/dx
    epsilon=1e-5
    M=int(length/dx)+1
    now=[-current[-1][1]]+list(current[-1])+[-current[-1][-2]]
    #now is a list with total length
    previous=current[-2]
    #next_ is a list which length is (total length-2-2)
    next_= \
        [ (2.-2.*r**2-6*epsilon*M**2)*center-pre_center+r**2*(1+4*epsilon*M**2)*(left1+right1)-epsilon*r**2*M**2*(left2+right2)
        for center,left1,left2,right1,right2,pre_center in zip(now[2:-3],now[1:-4],now[0:-5],now[3:-2],now[4:],previous[2:-3]) ]
    
    return [0.]+next_+[0.]
a=iterator(0.5,dt,init,update_rule)
print len(a)

b=[a_iter[2] for a_iter in a]
#b01=[a01_iter[5] for a01_iter in a01]
e=len(b)
#e01=len(b01)
d=linspace(0,0.01/300*e,e)
#d01=linspace(0,0.01/300*e01,e01)
#print d

y2=np.fft.fft(b)
f=np.fft.fftfreq(len(b),0.01/300)
y2=abs(y2)**2
plot(f,y2)
xlabel('Frequency(Hz)')
ylabel('Power(arbitrary units)')
title('Power spectrum')
show()
'''
y21=np.fft.fft(b01)
f01=np.fft.fftfreq(len(b01),0.01/300)
y21=abs(y21)**2
plot(f01,y21,':',color='r')
xlim(0,3000)
'''

