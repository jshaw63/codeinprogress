import math
import matplotlib.pyplot as plt

pi=math.pi
file=open("ode.txt","w")

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
 f=-math.sin(2.*a)-0.5*b
 return float(f)
#
# end of function definitions for now
#
tmin=0.
tmax=100.
nsteps=1000.

print 'tmin = ',tmin
print 'tmax = ',tmax

t_step=tstep(tmin,tmax,nsteps)
print 'tstep = ',t_step

t_val=t_values(tmin,tmax,t_step)
xorange=[-8,-5,-2,0,2,5,8]
yorange=[-2.,-1.75,-1.5,-1.25,-1,-0.75,-0.5,-0.25,-0.1,0,0.1,0.25,.5,0.75,1.,1.25,1.5,1.75,2.]
for k in range(len(xorange)):
  for j in range(len(yorange)):
    xo=xorange[k]
    yo=yorange[j]
    xn=[xo]
    yn=[yo]
#
    for i in range(len(t_val)-1):
      yavg=yn[i]+0.5*f(xn[i],yn[i])*t_step
      xnew=xn[i]+yavg*t_step
      yavg=0.5*(f(xnew,yavg)+f(xn[i],yn[i]))
      ynew=yn[i]+yavg*t_step
      file.write(str(xnew)+' '+str(ynew))
      file.write("\n")
      xn.append(xnew)
      yn.append(ynew)
    file.write("\n")
# plot graphs
file.close()


