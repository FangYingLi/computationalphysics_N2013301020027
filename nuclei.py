from pylab import*
import pickle

N=[]
t=[]
tau=0
dt=0
n=0
def ini(N,t,_tau,_dt,_n):
    global tau,dt,n
print "initial number of nuclei ->",
N.append(float(raw_input()))
print "time constant ->",
tau = float(raw_input()) 
print "time step ->",
dt = float(raw_input())
print "total time ->",
time = float(raw_input()) 
t.append(0)
n = int(time/dt)

def cal(N,t,tau,dt,n):
	print N,t,tau,dt,n
	for i in range(n):
		N.append(N[i]-N[i]/tau*dt)
		t.append(t[i]+dt)

def store(N,t,n):
	fout = open('output.txt','w')
for i in range(n):
	print >> fout,t[i],N[i]
	fout.close()									    
	
	pickle_file1=open("pickled_data.pkl","w")
	pickle.dump(t,pickle_file1)
	pickle.dump(N,pickle_file1)

def read():
    pickle_file1=open("pickled_data.pkl","r")
t=pickle.load(pickle_file1)
N=pickle.load(pickle_file1)
print t
print N

ini(N,t,tau,dt,n)
cal(N,t,tau,dt,n)
store(N,t,tau,dt,n)

plot(t,N,'g*-')
font={'color':'darked','weight':'normal','size':16}
title('Radioactive Decay')
ylabel('the number of uranium nuclei')
xlabel('time')

show()
savefig("nuclei_.jpg")
read()

