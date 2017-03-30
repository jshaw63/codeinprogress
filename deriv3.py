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
 f=math.exp(-a**2/6.)*math.sin(2.*a)/(2.*a)
 return float(f)
#
def y_values(x_values):
 y_values=[]
 for x in x_values:
   y=f(x)
   y_values.append(y)
 return y_values
#
def deriv(y,h):
  dydx=[]
  dd=(y[1]-y[0])/h
  dydx.append(dd)
  for i in range(1,len(y)-1):
   dd=(y[i+1]-y[i-1])/(2.*h)
   dydx.append(dd)
  dydx.append(dd)
  return dydx
#  
def integral(y,h):
  inty=[]
  ynew=0.
  for i in range(len(y)-1):
    ynew+=h/2.*(y[i+1]+y[i])
    inty.append(ynew)
  inty.append(ynew)
  return inty
#
def average(y):
  return sum([float(y[i]) for i in range(len(y))])/len(y)
#
def smooth(y):
  left=[(y[0]+y[1])/2.]
  mid=[(y[i-1]+2.*y[i]+y[i+1])/4. for i in range(1,len(y)-1)]
  right=[(y[i]+y[i+1])/2.]
  smooth=left+mid+right
  return smooth
#
def readdata(document, column):
  file=open(document,"r")
  lines=file.readlines()
  file.close()
  data=[]
  for line in lines:
    p=line.split()
    data.append(p[column])
  return data
#
def zeros(y):
  izero=[]
  for i in range(len(y)-1):
   sign=y[i]*y[i+1]
   if sign<=0.:
    izero.append(i)
  return izero


# end of function definition
#
xmin = -2.*pi
xmax=+2.*pi
nsteps=200

# main program
#
# define step size in x

xstep=xstep(xmin,xmax,nsteps)
#
# create list of x values
#
x_=x_values(xmin,xmax,xstep)
#
# create list of y values
#
y_ = y_values(x_)
#
# take derivative of function stored in y to
# get y' function
#
dydx=deriv(y_, xstep)
#
d2ydx2=deriv(dydx,xstep)
#
# integrate function stored in y to get
# antiderivative function
#
integrated=integral(y_,xstep)

avg=average(integrated)

shifted=[elem-avg for elem in integrated]

smoothed=smooth(dydx)

izeros=zeros(y_)
imaxmin=zeros(dydx)

print ' zeros of y at ',izeros
print ' zeros of dydx at ',imaxmin
for i in izeros:
  print 'y crossing between x= ',x_[i],' and x= ',x_[i+1]
for i in imaxmin:
  print 'max/min between x= ',x_[i],' and x= ',x_[i+1]

# plot graphs
#
plt.xlabel('x in radians w/ f(x) in red, df/dx in blue, integral of f(x) in green')
plt.grid(True)
plt.plot(x_,y_, color="red")
plt.plot(x_,dydx, color="blue")
plt.plot(x_,integrated, color="green")
plt.plot(x_,d2ydx2, color="yellow")
plt.show()

