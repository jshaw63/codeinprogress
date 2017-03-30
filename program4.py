# program prime		physics 104
# j. shaw		3/10/17
#
# prime test and factoring program
#
# input a number:
#
print ' prime number test and factoring program:'
print ' tests for primality and factors x if not prime'
x=float(input("enter x: "))
#
# echo back to screen
#
print 'You entered:'
print 'x = ',x
#
if x%2==0:
  print 'x = ',x,' is even'
if x%2==1:
  print 'x = ',x,' is odd'

# generates list of primes
#
nmax=10000
primes=[2,3]
for p in range(5,nmax):
  isprime='true'
  nxmax=int(p**0.5)+1
  for q in range(2,nxmax):
    remainder = p%q
    if remainder==0:
      isprime='false'
  if isprime=='true':
    primes.append(p)
#
# end primes list generation
#
# begin to test if x is prime and 
# generate list of factors if it is not prime
#
isprime='true'
factors=('')
for p in primes:
  remainder = x%p
  if remainder==0:
    isprime='false'
    reduced=x/p
    factors=factors+str(p)+'*'
    while reduced%p==0:
     factors=factors+str(p)+'*'
     reduced=reduced/p
  if x==p:
    isprime='true'
print 'x = prime is ',isprime
print 'factors= ',factors+'1'
#
# end of factoring algorithm
#
#




