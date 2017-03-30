import math
import matplotlib.pyplot as plt

pi=math.pi

# define functions

def xstep(xmin,xmax,nsteps):
  xstep=float(xmax-xmin)/nsteps
  return xstep

def x_values(xmin,xmax,xstep):
  x_list=[]
  x=xmin
  while x<=xmax:
   x_list.append(x)
   x=x+xstep
  return x_list
#
def f(a):
# f=math.exp(-a/5.)*math.cos(a)
  f=(math.sin(a))
  return float(f)
#
def y_values(x_values):
 y_values=[]
 for x in x_values:
   y=f(x)
   y_values.append(y)
 return y_values
#
def deriv(y,step):
  dydx=[]
  for i in range(len(y)-1):
   dd=(y[i+1]-y[i])/step
   dydx.append(dd)
  dydx.append(dd)
  return dydx

def integral(y,step):
   inty=[]
   for i in range(len(y)-1):
    temp=0.
    for j in range(i):
      temp+=(y[j+1]+y[j])/2.*step
    inty.append(temp)
   inty.append(temp)
   return inty
#
# end of function definition
#
xmin = -2.*pi
xmax=+2.*pi
nsteps=150

# main program calls functions
#
# define step size in x

xstep=xstep(xmin,xmax,nsteps)
#
# create list of x values in range of x
#
xx=x_values(xmin,xmax,xstep)
#
# create list of y values (calls y=f(x))
#
yy = y_values(xx)
#
# take derivative of function stored in y
#
dydx=deriv(yy, xstep)
#
# integrate function stored in y
#
integ=integral(yy,xstep)
# plot graphs
#
plt.plot(xx,yy, color="red")
plt.plot(xx,dydx, color="blue")
plt.plot(xx,integ, color="green")
plt.show()

