# program 1	physics 104
# j. shaw	3/9/17
# read and write from keyboard 
# demo program
#
# input two real numbers:
#
x=float(input("enter x: "))
y=float(input("enter y: "))
#
# echo back to screen
#
print 'You entered:'
print 'x= ',x,', y= ',y
#
sum=x+y
print 'sum = ',sum
#
print 'avg= ',sum/2.
#
if x%2==0:
  print 'x= ',x,' is even'
if x%2==1:
  print 'x= ',x,' is odd'
if y%2==0:
  print 'y= ',y,' is even'
if y%2==1:
  print 'y= ',y,' is odd'
#
# test if x < 31**2=961 is prime
# if x is prime it not a product 
# of smaller primes.  if it is not
# prime then it will be divided with
# zero remainder. The flag toggles
# false if the division works
#
isprime='true'
primes=(2,3,5,7,11,13,17,19,23,29,31)
for i in primes:
  remainder = x%i
  if remainder==0:
    isprime='false'
  if x==i:
    isprime='true'
print 'x = prime is ',isprime
#
# test if y < 31**2 is prime
#
isprime='true'
for i in primes:
  remainder = y%i
  if remainder==0:
    isprime='false'
  if y==i:
    isprime='true'
print 'y = prime is ',isprime
#
#
#




