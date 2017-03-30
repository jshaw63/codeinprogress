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
def f(a):
 f=-4.*pi**2*a+10.*a**3
 return float(f)
#
# end of function definitions for now
#
tmin=0.
tmax=2.
nsteps=100.

print 'tmin = ',tmin
print 'tmax = ',tmax

t_step=tstep(tmin,tmax,nsteps)
print 'tstep = ',t_step

t_val=t_values(tmin,tmax,t_step)

yorange=[0,.5,1.,1.5,2.,2.5,3.,3.5,4]
for j in range(len(yorange)):
  xo=0.
  yo=yorange[j]
  xn=[xo]
  yn=[yo]
  print xn
  print yn

  for i in range(len(t_val)-1):
    ystep=f(xn[i])*t_step
    ynew=yn[i]+ystep
    yavg=(ynew+yn[i])/2.
    xstep=yavg*t_step
    xnew=xn[i]+xstep
    xn.append(xnew)
    favg=(f(xn[i+1])+f(xn[i]))/2.
    ystep=favg*t_step
    ynew=yn[i]+ystep
    plt.scatter(xnew,ynew)
    yn.append(ynew)

# plot graphs

plt.grid(True)
plt.show()

