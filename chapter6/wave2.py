#This is a program about power spectrum of a string wave by lifangying
from matplotlib import animation
from pylab import*
import numpy as np
c=300.0
dx=0.01
l=np.linspace(0,1,100)

def w():
    y=[]
    dt=0.01/300
    t=0.0
    y0=np.exp(-1000*(l-0.5)**2)
    y.append(y0)
    y.append(y0)
    while t<0.05:
        y_next=np.zeros(100)
       
        for i in range(1,98):
            y_next[i]=-y[-2][i]+y[-1][i+1]+y[-1][i-1]
       
        y.append(y_next)
        t=t+dt
    return y, t
#print w()[0] ,w()[1]

y1=[]
def w2():
    t1=0.0
    dt1=0.01/300
    y_1=np.exp(-1000*(l-0.55)**2)
    y1.append(y_1)
    y1.append(y_1)
    while t1<0.05:
        y_next=np.zeros(100)
        for i in range(1,98):
            y_next[i]=-y1[-2][i]+y1[-1][i+1]+y1[-1][i-1]
        y1.append(y_next)
        t1=t1+dt1
    return y1, t1

a=w()[0]
a01=w2()[0]
#print cmp(a,a01)
'''
for iter in a01:
   print type(a01)
   '''
b=[a_iter[4] for a_iter in a]
b01=[a01_iter[4] for a01_iter in a01]
e=len(b)
e01=len(b01)
d=linspace(0,0.01/300*e,e)
d01=linspace(0,0.01/300*e01,e01)
#print d
'''
plot(d,b)
xlim(0,0.05)
xlabel('Time(s)')
ylabel('Signal(arbitary units)')
title('String signal versus time')
show()
'''
y2=np.fft.fft(b)
f=np.fft.fftfreq(len(b),0.01/300)
y2=abs(y2)**2
plot(f,y2)
xlim(0,3000)
xlabel('Frequency(Hz)')
ylabel('Power(arbitrary units)')
title('Power spectrum')
#show()
y21=np.fft.fft(b01)
f01=np.fft.fftfreq(len(b01),0.01/300)
y21=abs(y21)**2
plot(f01,y21,':',color='r')
xlim(0,3000)

show()
