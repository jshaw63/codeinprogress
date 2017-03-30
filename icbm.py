#program icbm			physics 104
# j. shaw			3/15/2017
#
# program uses user inputs to plot trajectories around
# earth for given initial latitude of launch, initial
# velocity, and initial angle
#
# import libraries
import math
import matplotlib.pyplot as plt
#
# create output file for data
file = open("icbm.txt", "w")
#
# constants
#
pi=math.pi
G=6.67e-11
M=5.96e24
k=G*M
re=6.376e6
small=1.e-3
tiny=1.e-6
deg2rad=pi/180.
rad2deg=180./pi
#
# input initial conditions from user
#
ro=float(input("enter initial ro in units of earth radii: "))
latitude=float(input("enter initial latitude of launch: "))
lat_rad=latitude*deg2rad
vo=float(input(" initial velocity in km/s: "))
vo=vo*1000
ro=ro*re
theta_o=float(input(" enter initial launch angle  from horizon in degrees: (0 to 180) "))
theta_o_rad=pi*theta_o/180.+small
#
# calculate energy and semimajor axis of orbit
#
pe=-k/ro
ke=0.5*vo**2
eo=ke+pe
a=-k/(2.*eo)
#
# calculate angular momentum and eccentricity of orbit
#
L=vo*ro*math.cos(theta_o_rad)
e=1.+2.*eo*L**2/k**2
e=math.sqrt(e)
if e<small:
  e=small
vesc=math.sqrt(2.*k/ro)
#
# echo data back to screen
#
print("\n")
print 'vo= ',vo/1000.,' km/s, vesc = ', vesc/1000.
print("\n")
print ' specific energy (J/kg) = ', eo
print ' specific angular momentum = ',L
print ' semi-major axis = ', a/re,' earth radii'
print ' eccentricity = ', e
print("\n")
#
# if initial data not consistent with elliptical orbit
# write message to user.  Skip to end of program.
#
if e>=1.0:
  print 'Parabolic or hyperbolic orbit for your initial cond.'
  print 'This program is not set up to handle escape orbits'
#
# if initial data consistent with elliptical orbit, continue
# with calculations and echo orbital parameters to screen
#
if e<1. :
  qo= (a*(1.-e**2)-ro)/(ro*e)
  qo = math.acos(qo)
  periapse=qo*rad2deg
  print 'The angle from periapse at t=0 is ', periapse
  print ' rmin = ', a/re*(1-e),' earth radii'
  print ' rmax = ', a/re*(1+e),' earth radii'
#
# set up subplot so I can plot both trajectory of icbm
# and draw the circle representing the earth on the same
# graph
#
  ax1 = plt.figure().add_subplot(111)
#
# define angular ranges and angle step size for loop
# then store angular range in list qrange. An improvment 
# to the program would separate the drawing angular range
# with constant qstep from the time integration of dq/dt
# for the motion of the projectile from momentum cons.
# Here I just use constant angular steps for drawing and 
# finding impact point when r<re.
#
  q=qo
  qmax=2.*pi
  npoints=180
  qstep=2.*pi/npoints
  qrange=[]
  while q<=qo+qmax:
   qrange.append(q)
   q=q+qstep
#   note: angles past the zenith have neg. qrange calc.
  if theta_o>90. :
    qo=-qo
    qstep=-qstep
    qmax=-qmax
    while q>=qo+qmax:
      qrange.append(q)
      q=q+qstep
#
# Now use the properly defined angular range to compute points
# on the orbit for graphics and file output.  x and y are
# coordinates of icbm. xr and yr are surface of the earth
# q is the angle on the orbit from periapse. qrel is position 
# angle of the projectile on the orbit s.t. qrel=lat at t=0
#
  rr=a/re*(1.-e**2)

  for q in qrange:
    r=rr/(1.+e*math.cos(q))
    xr=math.cos(q)
    yr=math.sin(q)
    qrel=lat_rad+q-qo
    x=r*math.cos(qrel)
    y=r*math.sin(qrel)
    file.write(str(x)+' '+str(y))
    file.write("\n")
#
    if r>= 1. :
      plt.scatter(x,y)
      qq=qrel
#
    ax1.scatter(xr,yr, color='brown')
#
# the relative angle at impact is stored in qq
# this angle is converted into final latitude and
# displayed to user
#
  northpole='false'
  southpole='false'
  qq_deg=qq*rad2deg
  lat_f=qq_deg
  if lat_f>90.:
    lat_f=180.-lat_f
    northpole='true'
  if lat_f<-90. :
    lat_f=-(180.+lat_f)
    southpole='true'
  print ''
  print 'impact at angle ',qq_deg,' degrees from equator'
  print 'at latitude ', lat_f
  if northpole=='true':
   print 'after crossing over the northpole is ',northpole
  if southpole=='true':
   print 'after crossing over the southpole is ',southpole
  print ''
#
# plot equator and poles on circle of earth
#
  plt.plot([-1,1],[0,0], lw=2, color='blue')
  plt.plot([0,0],[1,1.1], lw=2, color='green')
  plt.plot([0,0],[-1,-1.1], lw=2, color='green')
#
# end of if e<1 ifthen
# show plot if successful
#
  plt.show()
# close output files
file.close()


