print "Zeta function summation program"
# math libraries need to imported
import math
# define pi
pi=4.*math.atan(1.)
# insert power of 1/n^s
s=3
print " s= ", s
n=1
a=0
# set limit to sum and then do sum
nmax=100
while n <= nmax:
	an=1./n**s
        a=a+an
        print n, "series term= ", an, " partial sum = ", a
	n=n+1
print
# write out results
print "partial sum S_n=",a,"for n=",nmax
print
if s <= 1:
	print " series diverges for s = ",s
if s == 1:
	print " Harmonic Series"
if s > 1:
	print " series converges for s = ",s
        print
# use integral to bound limit above and below if convergent
	Iupper = (nmax)**(1-s)/(s-1)
	Ilower = (nmax+1)**(1-s)/(s-1)
# adding half range of bound on limit to Ilower gives average of interval
# as the correction to sum, R.
	R=(Iupper+Ilower)/2
	print "accelerated convergence S_n= ",a+R," for n= ",nmax
# Euler's result
if s == 2:
        L=pi**2/6.
	print "limit s=2 is S= ", L
        error = abs(a+R-L)
        print "error=", error
# Apery's result
if s == 3:
	L=1.202056903159594
	print "limit s=3 is S= ", L
        error =abs(a-L)
	print "error S_n=", error
        error = abs(a+R-L)
        print "errorS_n+R=", error
