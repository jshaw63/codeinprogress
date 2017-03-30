print "iterative solution for square root of 2"
n=0
a=1
eps=1
while eps > 1e-8:
	print n,a,eps
	an=2.+1./a
	n=n+1
	eps=abs(an-a)
	a=an
print "x=",an-1.,"n=",n
