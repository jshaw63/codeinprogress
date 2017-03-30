def average(inlist):
  return sum([float(inlist[i]) for i in range(len(inlist))])/len(inlist)

p=[1,2,3,4]
pavg=average(p)
print 'p= ',p,' the average of p is pavg= ', pavg

