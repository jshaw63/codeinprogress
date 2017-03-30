import math
import matplotlib.pyplot as plt
#
x=0;xstep=0.25;xmax=7.
xvalues=[]
while x <= xmax:
   xvalues.append(x)
   x=x+xstep
#
print 'xvalues= ', xvalues
#
yvalues=[]
for x in xvalues:
 y=math.sin(x)
 yvalues.append(y)
 plt.scatter(x,y)
#
print 'yvalue= ', yvalues
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
