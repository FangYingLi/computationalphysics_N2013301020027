#This is a program about power spectrum of a string wave by lifangying
""" Docstring: used to indicate the purpose of the code:
    Simulate the vibration on piano string.
        :W1     condition...
        :W2     condition...
"""
from matplotlib import animation
from pylab import*
import numpy as np

epsilon = 1e-5
c_const=300.0
dx=0.01
dt = dx/c_const
length = 1.0
string = np.linspace(0.,length,1+int(length/dx))


def iterator(stop_time, t_interval, init_cond, update_rule):
    """ iterate the string with update_rule
        : stop_time          simulation time
        : t_interval    length of time step
        : init_cond     initial array
        : update_rule   called upon at each simulation
    """
    result = [init_cond, init_cond]
    time = 0
    while time < stop_time:
        result.append(update_rule(result[-2:], t_interval))
        time+=t_interval
    del result[0] # remove the redundant initial condition
    return result

def update_rule(array_curr, t_interval):
    """ periodic boundary condition
    """
    # constants used in calculation
    r = c_const * t_interval/dx
    M = length/dx
    # prepare array for iteration
    array_now = \
        [array_curr[-1][1]]+list(array_curr[-1])+[array_curr[-1][-2]]
    # padding the current array
    array_prev = array_curr[-2]
    borderless = [
        (2.-2.*r**2.-6.*epsilon*r**2.*M**2.)*center - up +
        r**2.*(1.+4.*epsilon*M**2.)*(right_1+left_1) -
        epsilon*r**2.*M**2.*(right_2+left_2)
        for center, left_1, left_2, right_1, right_2, up in
        zip(array_now[2:-2], array_now[1:-3], array_now[0:-4], array_now[3:-1],
            array_now[4:], array_prev)]
    return [0.] + borderless + [0.]     # padding the boundary condtion.

def fix_boundary_rule(array_curr, t_interval):
    """ fixed boundary condition """
    array_now = array_curr[-1]
    array_prev = array_curr[-2]
    return [0.] + [-up + right + left
                  for up, right, left in 
                  zip(array_prev, array_now[2:], array_now[0:-2])
                 ] + [0.]

# initialize array
init_array = np.exp(-1000.*(string-0.55)**2)
init_array[0] = init_array[-1] = 0.

a=iterator(stop_time=0.05, t_interval=dt, init_cond=init_array,
           update_rule=update_rule)
a01=iterator(stop_time=0.05, t_interval=dt, init_cond=init_array,
             update_rule=fix_boundary_rule)
#print cmp(a,a01)
'''
for iter in a01:
   print type(a01)
   '''
b=[a_iter[5] for a_iter in a]
b01=[a01_iter[5] for a01_iter in a01]
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
xlabel('Frequency(Hz)')
ylabel('Power(arbitrary units)')
title('Power spectrum')
show()

y21=np.fft.fft(b01)
f01=np.fft.fftfreq(len(b01),0.01/300)
y21=abs(y21)**2
plot(f01,y21,':',color='r')
xlim(0,3000)


