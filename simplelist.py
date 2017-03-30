# List Examples:				physics 104
# J. Shaw						3/22/17
#
# This program uses lists in various ways which
# may be useful in solving programming problems
# 

import math
pi=math.pi

list=('Bach','Beethoven','Brahms')
nitems=len(list)
print 'there are ',nitems,' items in this list:'

for i in range(nitems):
  print 'list[',i,']= ',list[i]
#
print ' '
#
irange=range(-10,10)
print 'integers in list = ',irange
ylist=[]
for i in irange:
 y=i**2
 print i,y
 ylist.append(y)
#
print 'squared integers in list = ',ylist
print ' '

def average(in_list):
  return sum([float(in_list[i]) for i in range(len(in_list))])/len(in_list)

print 'The average of ',irange, ' is ',average(irange)

print ' '
#
# 2-D vector math done with list manipulations 
#
A=(-1,2)
B=(-3,-4)
#
print 'A= ',A
print 'B= ',B
#
ndim=len(A)
dot=0; Amag=0.;Bmag=0.
for i in range(ndim):
  dot+=A[i]*B[i]
  Amag+=A[i]*A[i]
  Bmag+=B[i]*B[i]
Amag=Amag**0.5; Bmag=Bmag**0.5
print 'dot = ',dot
print '|A|= ',Amag
print '|B|= ',Bmag
angle=math.acos(dot/(Amag*Bmag))
print 'angle between A and B= ',angle*180./pi,' degrees'
#
def dot_product(a,b):
 return sum([a[i]*b[i] for i in range(len(a))])
#
def mag_vector(a):
  return (sum([a[i]*a[i] for i in range(len(a))]))**0.5
#
dot = dot_product(A,B)
print 'dot = ',dot
#
Amag=mag_vector(A)
print '|A| = ',Amag
Bmag=mag_vector(B)
print '|B| = ', Bmag
#
def vector_sum(a,b):
  c=[]
  for i in range(len(a)):
    c.append(a[i]+b[i])
  return c
#  
absum=vector_sum(A,B)
print 'A+B = ', absum
#
j=0
cross = 0
while j< ndim:
 i=0
 while i < ndim:
  if i<j:
   sign=+1.
  elif i>j:
   sign=-1.
  elif i==j:
   sign=0.
  cross = cross+sign*A[i]*B[j]
  i+=1
 j+=1
print 'cross = ', cross
#
C=[]
for i in range(ndim):
 C.append(A[i]+B[i])
print 'sum A + B = C => C =',C
angle=math.atan2(C[1],C[0])
print 'angle of C from x-axis = ', angle*180./pi,' degrees'
#
print ' '
#

def word_count(document, text):
 print 'reading document = ',document
 print 'scanning for word ', text,':'
 file=open(document,"r")
 lines=file.readlines()
 file.close()
 n=0
 i=0
 for line in lines:
   i=i+1
   p=line.split()
   for j in range(len(p)):
    if p[j] == text:
     n=n+1
     print text,' occurs in line',i,' at position ',j
 print 'The word ',text,' occurs ',n,' times in this document'
 print ' '

document='1989-Bush.txt'
word='American'
word_count(document,word)
  




