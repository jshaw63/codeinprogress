print "plotting program for series approximations"
# math libraries need to imported
import math
import cmath
import Gnuplot, Gnuplot.funcutils
gg = Gnuplot.Gnuplot(debug=1, persist=1)

# define pi and Ij
pi=4.*math.atan(1.)
Ij=complex(0.,1.)
#
# create an output file for graphing
#
file = open("series.txt", "w")
# set up data range and step sizes for x
Range=4.*pi
nsteps=1000
xstep=Range/nsteps
xmin=-2.*pi
xmax=xmin+Range
tiny=1.e-6
# set up the power series parameters m
mmax=10
#
# loop over x and calculate f(x)'s
#
# here I compute f(x) =exp(I x/2) (log(I cot(x/4)))-exp(-I x/2) (log(-I cot(x/4))))/(4 I)
# simplifying log terms further gave problems. phase error? This expression
# works for HW1 problem.  Change f(x) and g(x) to fit needs
n=0
while n <= nsteps:
	x=xmin+n*xstep+tiny
	exp1=cmath.exp(Ij*x/2.)
	exp2=cmath.exp(-Ij*x/2.)
	log1=cmath.log(Ij/math.tan(x/4.))
        log2=cmath.log(-Ij/math.tan(x/4))
	f=(exp1*log1-exp2*log2)/(4.*Ij)
        n=n+1
#  calculate power series at x, g(x) while still inside loop
        m=0
	g=0.
	while m <=mmax:
		g=g+math.sin(m*x)/(2.*m-1.)
		m=m+1
#	print x,' ',f,' ',g
        file.write(str(x))
        file.write(str(' '))
	file.write(str(f.real))
        file.write(str(' '))
        file.write(str(g))
        file.write("\n")
# exit loops
#
# exit program
file.close()
#
# plot results using:
gg('plot "series.txt" using 1:2 with lines, "series.txt" using 1:3 with lines')
#

	


