import math
import matplotlib.pyplot as plt
x=0
while x in xrange(0,10):
 y=x**2
 plt.scatter(x,y)
 x=x+1
plt.xlabel('x')
plt.ylabel('y')
plt.show()
