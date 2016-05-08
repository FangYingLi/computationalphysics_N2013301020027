from visual import *
def g(r,p):#(radius,period)
    return vector(0,2*pi*r/p,0)#get velocity vector,(0,vy,0)

#draw five stationary spheres,which their position,color,size
mercury=sphere(pos=(0.39,0,0),color=color.blue,radius=0.06,make_trail=True)
venus=sphere(pos=(0.72,0,0),color=color.yellow,radius=0.06,make_trail=True)
earth=sphere(pos=(1.0,0,0),color=color.green,radius=0.06,make_trail=True)
mars=sphere(pos=(1.52,0,0),color=color.red,radius=0.06,make_trail=True)
sun=sphere(pos=(0,0,0),color=color.orange,radius=0.2,make_trail=True)

mercury.v=g(0.39,0.241)#v means velocity
venus.v=g(0.72,0.615)
earth.v=g(1,1)
mars.v=g(1.52,1.88)

dt=0.001
while True:
    rate(200)
    for i in [mercury,venus,earth,mars]:
#consider the dynamic equation
        r=sqrt((i.x)**2+(i.y)**2)
        i.v=i.v-vector(4*pi**2*i.x*dt/r**3,4*pi**2*i.y*dt/r**3)
        i.pos=i.pos+(i.v[0]*dt,i.v[1]*dt,0)#v[0] is vx, v[1] is vy


