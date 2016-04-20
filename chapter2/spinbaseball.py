import math
import matplotlib.pyplot as plt
# import modules above
g=9.8
omega=4000*math.pi/60
vd=35
v_wind=3
Delta=5
S0m=0.00041#it means s0/m
# B2m=0.00004
# y_zero=10000
# a=0.0065
# T0=300
# alpha=2.5
class baseball:
    def __init__(self,v0,theta,yFinal=0):
        self.x0=0
        self.y0=1.8
        self.yFinal=yFinal
        self.v0=v0
        self.Theta=theta
        self.theta=theta*math.pi/180
        self.vx0=self.v0*math.cos(self.theta)
        self.vy0=self.v0*math.sin(self.theta)
        self.dt=0.01
        return None
    
    def B2m(self,v):#it means B2/m
        return 0.0039+0.0058/(1+math.exp(v-vd/Delta))
    def F(self,vx,vy):
        vxy=math.sqrt(vx**2+vy**2)
        Fx=-self.B2m(vxy)*math.sqrt((vx-v_wind)**2+vy**2)*(vx-v_wind)-S0m*omega*vy
        Fy=-self.B2m(vxy)*math.sqrt((vx-v_wind)**2+vy**2)*vy+S0m*omega*vx
        return Fx,Fy
    def fly(self):
        self.X=[self.x0]
        self.Y=[self.y0]
        self.Vx=[self.vx0]
        self.Vy=[self.vy0]
        self.T=[0]
        while not (self.Y[-1]<self.yFinal and self.Vy[-1]<0):
            newVx=self.Vx[-1]+self.F(vx=self.Vx[-1],vy=self.Vy[-1])[0]*self.dt
            newVy=self.Vy[-1]-g*self.dt+self.F(self.Vx[-1],self.Vy[-1])[1]*self.dt
            self.Vx.append(newVx)
            self.Vy.append(newVy)
            meanVx=0.5*(self.Vx[-1]+self.Vx[-2])
            meanVy=0.5*(self.Vy[-1]+self.Vy[-2])
#            meanV=math.sqrt(meanVx**2+meanVy**2) # not used in Cannon0 because there is no air drag
            newX=self.X[-1]+meanVx*self.dt
            newY=self.Y[-1]+meanVy*self.dt
            self.X.append(newX)
            self.Y.append(newY)
        # fix the final landing coordinate        
#        r=-self.Y[-2]/self.Y[-1]
        self.X[-1]=((self.Y[-2]-self.yFinal)*self.X[-1]+(self.yFinal-self.Y[-1])*self.X[-2])/(self.Y[-2]-self.Y[-1])
        self.Y[-1]=self.yFinal
        return 0
    # get the final distance shells can reach
    def distance(self):
        return self.X[-1]
    def height(self):
        return max(self.Y)
    # represent trajectory 
    def plot_2d(self, color):
        plt.plot(self.X,self.Y,color,label="$%dm/s$,$%d\degree$, with backspin"%(self.v0,self.Theta))
        legend(loc='best')
        return 0
'''    def trace(self):
        global x,y
        x=[]
        y=[]
        for t in self.'''
class baseball1(baseball):
    "the second simplest model with no air drag under constant air density, no probability distribution"    
    # external force other than gravity        
    def F(self,vx,vy,y=1):
        vxy=math.sqrt(vx**2+vy**2)
        Fx=-self.B2m(vxy)*math.sqrt((vx-v_wind)**2+vy**2)*(vx-v_wind)
        Fy=-self.B2m(vxy)*math.sqrt((vx-v_wind)**2+vy**2)*vy
        return Fx,Fy
    def plot(self, color):
        plt.plot(self.X,self.Y,color,label="$%dm/s$,$%d\degree$, no backspin"%(self.v0,self.Theta))
        return 0
        
# select the angle casting the largest distance
import numpy as np

theta=np.linspace(15,75,12)
f=[]
for i in range (len(theta)):
    k=baseball(41.6,theta[i],0)
    k.fly()
    plt.plot(k.X,k.Y,label=r'$\theta=%.2f^\circ$'%theta[i])
    plt.xlabel('the initial angle/deg')
    plt.ylabel('the maximum range/m')
    plt.title('the maximum ranges at different initial angles')
    plt.legend(loc='best',frameon=False)
    f.append(k.X[-1])
    
plt.show()

phi=np.linspace(13.5,73.5,12)
width=3
plt.bar(phi,f,width,color='r')
plt.xlabel(r'$\theta^\circ$')
plt.ylabel('the maximum range')
plt.title('the maximum ranges at different initial angles')
plt.show()


'''A=baseball(100,45)
A.fly()
A.plot('g')

B=baseball1(100,45)
B.fly()
B.plot('b')
plt.legend(loc='upper right',frameon=False)
plt.show()

print A.distance()
print A.height()
print B.distance()
print B.height()
'''
