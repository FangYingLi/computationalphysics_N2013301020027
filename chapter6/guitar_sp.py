#This is a program about power spectrum of a string wave by lifangying
from matplotlib import animation
from pylab import*
import numpy as np
c=320.0
dx=6.5*1e-4
l=np.linspace(0,0.65,1000)

def w():
    y=[]
    dt=dx/c
    t=0.0
    y0=np.exp(-1000*(l-l*0.2)**2)
    y.append(y0)
    y.append(y0)
    while t<0.05:
        y_next=np.zeros(1000)
       
        for i in range(1,998):
            y_next[i]=-y[-2][i]+y[-1][i+1]+y[-1][i-1]
       
        y.append(y_next)
        t=t+dt
    return y, t
#print w()[0] ,w()[1]

y1=[]
def w2():
    t1=0.0
    dt1=dx/c
    y_1=np.exp(-1000*(l-l*0.05)**2)
    y1.append(y_1)
    y1.append(y_1)
    while t1<0.05:
        y_next=np.zeros(1000)
        for i in range(1,998):
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
b=[a_iter[800] for a_iter in a]
b01=[a01_iter[950] for a01_iter in a01]
print len(b)
e=len(b)
e01=len(b01)
d=linspace(0,dx/c*e,e)
d01=linspace(0,dx/c*e01,e01)
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

f=np.fft.fftfreq(len(b),dx/c)
y2=abs(y2)**2
#print f,len(y2)
plot(f,y2)
xlim(0,6000)
xlabel('Frequency(Hz)')
ylabel('Power(arbitrary units)')
title('Guitar Power spectrum:Pluck at 1/5')
show()

y21=np.fft.fft(b01)
f01=np.fft.fftfreq(len(b01),dx/c)
y21=abs(y21)**2
plot(f01,y21,color='r')
xlim(0,12000)
xlabel('Frequency(Hz)')
ylabel('Power(arbitrary units)')
title('Guitar Power spectrum:Pluck at 1/20')
show()
