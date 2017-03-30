# program primes	physics 104
# j. shaw		3/9/17
# 
# generates list of primes
#
nmax=1000
primes=[2,3]
for x in range(5,nmax):
  isprime='true'
  nxmax=int(x**0.5)+1
  for y in range(2,nxmax):
    remainder = x%y
    if remainder==0:
      isprime='false'
  if isprime=='true':
    primes.append(x)
#
print 'primes= ',primes
#
# end of program
#




