from visual import *
#my first vpython program!
scene.title='binary star'
scene.forward=vector(0,-0.3,-1)

G=6.7e-11

b=sphere(pos=(-1e11,0,0),color=color.red,radius=4e10)
b.make_trail=True
b.p=vector(0,0,-1e4)*2e30#p=mv
b.mass=2e30

s=sphere(pos=(1.5e11,0,0),color=color.blue,radius=2e10,make_trail=True)
s.p=-b.p
s.mass=1e30

dt=1e5
while True:
    rate(200)
    dist=s.pos-b.pos
    force=G*b.mass*s.mass*dist/pow(mag(dist),3)#gravity,mag means sqrt(x**2+y**2+z**2),pow means power function,pow(x,y)=x**y
    b.p=b.p+force*dt#p=p+F*dt
    s.p=s.p-force*dt
    b.pos=b.pos+b.p/b.mass*dt#pos=pos+v*dt
    s.pos=s.pos+s.p/s.mass*dt


