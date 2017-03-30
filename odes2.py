import math
import matplotlib.pyplot as plt

pi=math.pi

# define functions

def tstep(tmin,tmax,nsteps):
  tstep=float(tmax-tmin)/nsteps
  return tstep

def t_values(tmin,tmax,tstep):
  t_list=[]
  t=tmin
  while t<=tmax:
   t_list.append(t)
   t+=tstep
  return t_list
#
def f(a,b):
 f=-math.sin(2.*a)-0.15*b
 return float(f)
#
# end of function definitions for now
#
tmin=0.
tmax=30.
nsteps=300.

print 'tmin = ',tmin
print 'tmax = ',tmax

t_step=tstep(tmin,tmax,nsteps)
print 'tstep = ',t_step

t_val=t_values(tmin,tmax,t_step)

yorange=[-2.,-1.5,-1,-0.5,-0.25,0, 0.25,.5,1.,1.5,2.]
for j in range(len(yorange)):
  xo=-1.5
  yo=yorange[j]
  xn=[xo]
  yn=[yo]
#
  for i in range(len(t_val)-1):
    yavg=yn[i]+0.5*f(xn[i],yn[i])*t_step
    xnew=xn[i]+yavg*t_step
    xn.append(xnew)
    yavg=0.5*(f(xnew,yavg)+f(xn[i],yn[i]))
    ynew=yn[i]+yavg*t_step
    plt.scatter(xnew,ynew)
    yn.append(ynew)

# plot graphs

plt.grid(True)
plt.show()

