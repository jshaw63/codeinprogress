print "plotting program for special functions: Bessel Example"
# math libraries need to imported
import math
import cmath
import numpy as np
import scipy as sp
from scipy import constants
from scipy import special
# define pi and Ij
pi=4.*math.atan(1.) # may not be needed with constants imported
Ij=complex(0.,1.)
#
# create an output file for graphing
#
file = open("series.txt", "w")
# set up data range and step sizes for x
Range=4.*pi
nsteps=1000
xstep=Range/nsteps
xmin=0
xmax=xmin+Range
tiny=1.e-6
# set up the power series parameters r if needed
rmax=5
#
# loop over x and calculate f(x)'s
#
# Change f(x)'s and g(x)'s to fit needs
n=0
while n <= nsteps:
	x=xmin+n*xstep+tiny
# built in Bessel function calls
        f0=sp.special.jv(0,x)
        f1=sp.special.jv(1,x)
	f2=sp.special.jv(2,x)
        n=n+1
#  calculate power series at x while still inside loop, diverges x> 1. Check
# Numerical recipes for better approximation or tricks for stable algorithm
        r=0
	f=0.
	g=0.
#	while r <=rmax:
#                f=f+((-1)**r/(math.factorial(r)*math.factorial(r)))*(x/2.)**(2*r)
#                g=g+((-1)**r/(math.factorial(r)*math.factorial(1+r)))*(x/2.)**(1+2*r)
#		r=r+1
	print x,' ',f0,' ',f1,' ',f2
        file.write(str(x))
        file.write(str(' '))
	file.write(str(f0))
        file.write(str(' '))
        file.write(str(f1))
 	file.write(str(' '))
        file.write(str(f2))
        file.write("\n")
# exit loops
#
# exit program
file.close()
#
# plot results using gnuplot with command:
# plot "series.txt" using 1:2 with lines, "series.txt" using 1:3 with lines, "series.txt" using 1:4 with lines
	


