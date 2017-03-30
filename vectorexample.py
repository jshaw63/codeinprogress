def vector_sum(a,b):
  c=[]
  for i in range(len(a)):
    c.append(a[i]+b[i])
  return c

A=[1,2]
B=[3,4]
vectorsum=vector_sum(A,B)
print vectorsum

