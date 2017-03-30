#program orbit			physics 104
# j. shaw			3/22/2017
#
# program uses user inputs to plot trajectories around
# earth for given initial latitude of launch, initial
# velocity, and initial angle.  differs from icbm in that
# time is independent variable so non-impact and open
# orbits are allowed.
#
# import libraries
import math
import matplotlib.pyplot as plt
#
# create output file for data
file = open("orbit.txt", "w")
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
#
# convert km/s to meters/s and earth radii to meters
vo=vo*1000
ro=ro*re
#
theta_o=float(input(" enter initial launch angle from local horizon in degrees: (0 to 180) "))
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
print 'vo= ',vo/1000.,' km/s'
print 'vesc = ', vesc/1000.
print 'vc= ', vesc/math.sqrt(2.)/1000.,' km/s'
print("\n")
print ' specific energy (J/kg) = ', eo
print ' specific angular momentum = ',L
print ' semi-major axis = ', a/re,' earth radii'
print ' eccentricity = ', e
print("\n")
#
# if initial data consistent with elliptical orbit, continue
# with calculations and echo orbital parameters to screen
#
if e<1. :
  p=a*(1.-e**2)
  qo= (p-ro)/(ro*e)
  qo = math.acos(qo)
  periapse=qo*rad2deg
  print 'The angle from periapse at t=0 is ', periapse
  print ' rmin = ', a/re*(1-e),' earth radii'
  print ' rmax = ', a/re*(1+e),' earth radii'
  period=math.sqrt((4.*pi**2/k)*a**3)
  print 'Kepler period = ', period/3600., ' hours = ', period/86400.,' days'
  qmax=2.*pi
  npoints=360
  tstep=period/npoints
  while tstep>1000.:
   tstep=tstep/2.
  tmax=period
  rr=p/re
elif e>1. :
  a=-a
  p=a*(e**2-1.)
  print ' a= ',a,' e= ',e,' p= ',p/re,' earth radii'
  qo=(a*(e**2-1.)-ro)/(ro*e)
  print 'q0= ',qo
  qo=math.acos(qo)
  periapse=qo*rad2deg
  print 'The angle from periapse at t=0 is ', periapse
  print 'rmin= ',a/re*(e-1.)
  print 'rmax undefined for escape orbits'
  print 'Kepler period undefined for escape orbits'
  qmax=pi-small
  npoints=360
  days=86400.
  tstep=days/npoints
  while tstep>1000.:
   tstep=tstep/2.
  tmax=0.5*days
  rr=p/re
#
# set up subplot so I can plot both orbit and 
# draw the circle representing the earth on the same
# graph
#
ax1 = plt.figure().add_subplot(111)
qr=0.
qrstep=2.*pi/200
while qr< 2.*pi:
    xr=math.cos(qr)
    yr=math.sin(qr)
    ax1.scatter(xr,yr, color='brown')
    qr=qr+qrstep
#
# Now x and y are coordinates on the orbit of the space craft,
# q is the angle on the orbit from periapse. qrel is position 
# angle of the space craft on the orbit s.t. qrel=lat at t=0
#

q=qo
r=ro
qstep=(L/ro**2)*tstep
#
# echo back to screen
#
print ' '
print 'At t=0, the starting values are:'
print 'angle from periapse=', q,' radians'
print 'radial distance from earth = ', r/re,' earth radii = ', r,' meters'
print 'angular step size is qstep = ', qstep,' in radians,'
print ' time step= ', tstep,' seconds'
print 'angular velocity ~ ', qstep/tstep,' rad/s, v_t~ ', qstep/tstep*r*math.cos(theta_o_rad)/1000,' km/s.'

nstep=0
t=0
while t < tmax:
  r=rr/(1.+e*math.cos(q))
  qrel=lat_rad+q-qo
  x=r*math.cos(qrel)
  y=r*math.sin(qrel)
  file.write(str(nstep)+' '+str(t)+' '+str(x)+' '+str(y)+' '+str(r)+' '+str(q)+' '+str(qstep))
  file.write("\n")
  qstep=(L/(r*re)**2)*tstep
  q=q+qstep
  nstep=nstep+1
  if r>= 1. :
    plt.scatter(x,y)
    qq=qrel
    t=t+tstep
  else:
    t=tmax
#
#
# the relative angle at impact is stored in qq
# this angle is converted into final latitude and
# displayed to user
#
if r< 1. :
  print ' '
  print 'impact with earth for your initial conditions:'
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
# show plot if successful
#
plt.show()
# close output files
file.close()


