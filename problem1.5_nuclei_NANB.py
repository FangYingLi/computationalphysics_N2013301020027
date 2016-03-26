#this is a program describes a system that likes a resonance#
#by Li FangYing March 24#

from pylab import*
import pickle
import math

na=[]
nb=[]
t=[]
tau=0
dt=0
n=0
def ini(na,nb,t,ttau,ddt,nn):
	global tau,dt,n#if don't insert global,we cannot change the value of tau,dt,n outside the function,the picture is a blank#
#besides,you don't need to global total time,because it's connected with n#
	na.append(100)
	nb.append(0)
	print "time constant ->",
	tau = float(raw_input()) 
	print "time step ->",
	dt = float(raw_input())
	print "total time ->",
	time = float(raw_input()) 
	t.append(0)#t is different from time,it is accumulated by 0+n*dt#
	n = int(time/dt)

ta=[]
tb=[]
def cal(na,nb,ta,tb,tau,dt,n):
	C = (na[0]-nb[0])/2
	D = (na[0]+nb[0])/2
	for i in range(n):
		na.append(na[i] + ((nb[i]/tau)-(na[i]/tau))*dt)
		nb.append(nb[i] + ((na[i]/tau)-(nb[i]/tau))*dt)
		ta.append(C*math.exp(-t[i]*2/tau)+D)#ta,tb mean the true value of na,nb,which are solved precisely#
		tb.append(-C*math.exp(-t[i]*2/tau)+D)
		t.append(t[i]+dt)
	ta.append(50.0)#!!must keep the dimension of t and ta the same,len(t)=time/dt+1=len(na),and len(ta)=time/dt, so append one more value to ta  
	tb.append(50.0)

ini(na,nb,t,tau,dt,n)
cal(na,nb,ta,tb,tau,dt,n)

print len(t),len(na),len(ta)
print t,na,ta

plot(t,na,'g*',label='NA(numerical)')
plot(t,nb,'r*',label='NB(numerical)')
plot(t,ta,'b',label='NA(true value)')
plot(t,tb,'k',label='NB(true value)')
legend(loc = 'lower center',fontsize = 8)
title('Radioactive Decay between two kinds of nuclei')
ylabel('the number of nuclei')
xlabel('time/s')
text(0.3,0.8*na[0],'Time Constant='+str(tau)+'s'+'\n'+'Time Step ='+str(dt)+'s')
show()

