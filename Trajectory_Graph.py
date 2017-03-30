#import libraries
import math
import matplotlib.pyplot as plt
#define constants, variables, and functions
pi=math.pi
v=float(input("enter v"))
theta=float(input("enter theta"))
Hi=float(input("enter Hi"))
Hf=float(input("enter Hf"))
theta_rad=pi*theta/180.
vx=v*math.cos(theta_rad)
vy=v*math.sin(theta_rad)
g=9.81
y0=Hi
t=0
deltaH=Hf-Hi
v0y=vy
t_top=v0y/g
v0x=vx
#
timpact=t_top+(math.sqrt(v0y**2-4*(-g/2)*(-deltaH))/g)
x_range=vx*timpact
v0=0
t_0=0
T_end=timpact
###Hf=(-g/2*t**2)+(v0y*t)+Hi
#end of constants,variables, and functions

#graph start

t=0; tstep=0.05;tmax=T_end
tvalues=[]
while t<= tmax:
	tvalues.append(t)
	t=t+tstep
for t in tvalues:
        x=v0x*t
	y=(-g/2*t**2)+(v0y*t)+y0
	plt.scatter(x,y) #Graphs function as a scatter plot

#graph end

#display results
print 'you entered v= ',v,' and theta= ',theta
print 'vx= ',vx,' vy= ',vy
print'the range is ', xrange, ' meters'
print'time of  flight = ', timpact
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
