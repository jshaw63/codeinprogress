# program 5	physics 104
# j. shaw	3/12/17
# 
# trajectory problem
#
# import libraries
#
import math
import Gnuplot, Gnuplot.funcutils
gnu = Gnuplot.Gnuplot(debug=1, persist=1)
import matplotlib.pyplot as plt
#
#
# create an output file for graphing
#
file = open("traj.txt", "w")
#
# define constants
#
g=9.81
#
# begin program input
# input initial velocity and angle:
#
print ' simple trajectory program (level1 to level2)'
print ' input a velocity and angle to find range'
v=float(input("enter  initial velocity (m/s): "))
theta=float(input("enter  initial launch angle (degrees): "))
theta_rad=math.pi*theta/180.
#
# echo back to screen
#
print 'You entered:'
print 'v= ',v,' m/s, theta=',theta,' degrees.'
#
vx=v*math.cos(theta_rad)
vy=v*math.sin(theta_rad)
#
print 'enter height at launch h_i='
h_i=float(input("h_i= "))
print 'enter height at impact h_f='
h_f=float(input("h_f="))
dh=h_f-h_i
#
rise_time=vy/g
x_rise=vx*rise_time
max_height=-g/2.*rise_time**2+vy*rise_time+h_i
time_of_flight=vy/g+math.sqrt(vy**2+2.*g*(-dh))/g
x_range=vx*time_of_flight
vx_impact=vx
vy_impact=-g*time_of_flight+vy
v_impact =math.sqrt(vx_impact**2+vy_impact**2)
theta_impact = 180.*math.atan2(vy_impact,vx_impact)/math.pi
#
print ''
print ' The projectile is in the air for ', time_of_flight,' seconds'
print ' and the impact point is ', x_range,' meters from launch.'
print ' The projectile speed at impact is ', v_impact,' m/s and the impact angle'
print ' is ', theta_impact,' degrees. The peak of the trajectory was'
print ' at x= ', x_rise,' and y= ',max_height,' meters.'
print ''
#
# export data for plotting
#
file.write('#  time:     distance:     height:     level:')
file.write("\n")
#
npoints=200
time_step=time_of_flight/npoints
t=0.
while t <= time_of_flight:
  x=vx*t
  y=-g/2.*t**2+vy*t+h_i
  if x<x_rise:
   yo=h_i
  else:
   yo=h_f
#
  file.write(str(t)+' '+str(x)+' '+str(y)+' '+str(yo))
  file.write("\n")
  plt.scatter(x, y)
  t=t+time_step

# plot data to gnuplot
#  close file _first_ to make sure all data read...
file.close()
gnu('set xlabel "distance(meters)" ')
gnu('set ylabel "height(meters)" ')
gnu('plot "traj.txt" using 2:3 title "trajectory" with lines, "traj.txt" using 2:4 title "surface" with lines lw 3')
#
# plot data using pyplot
#
plt.xlabel('distance(meters)')
plt.ylabel('height(meters)')
plt.grid(True)
plt.show()
#







