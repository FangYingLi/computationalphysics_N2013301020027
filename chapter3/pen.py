import numpy as np
from math import *
from pylab import *
a=2.007089923
theta=np.linspace(0,90,90)
t=[]
for i in range(len(theta)):
    t.append(a*(1+0.25*sin(theta[i]/57.3)**2))
print t
plot(theta,t,lw=1.5)
xlabel('A/'+r'$^{\circ}$')
ylabel('t/s')
title('the amplitude-period relation')
show()
