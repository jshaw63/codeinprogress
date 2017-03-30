def vector_cross(a,b):
  c=[]
#
  if len(a)==3:
    c.append(a[1]*b[2]-a[2]*b[1])
    c.append(a[0]*b[2]-b[0]*a[2])
    c.append(a[0]*b[1]-a[1]*b[0])
  elif len(a)==2:
    c.append(0)
    c.append(0)
    c.append(a[0]*b[1]-a[1]*b[0])
  else:
    print 'n must 2 or 3 for cross product'
#
  return c

A=[1,6]
B=[4,0]

C=vector_cross(A,B)
print ' ',A,' X ',B,' = ',C,' = ',C[0],'i+',C[1],'j+',C[2],'k'
