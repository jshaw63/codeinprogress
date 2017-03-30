import csv
import matplotlib.pyplot as plt

file = open("input.csv", "rb")
reader = csv.reader(file, delimeter=",")

xlist=[]
ylist=[]
lineskip=0
i=0
for row in reader:
  if i>=lineskip:
   x,y=float(row[0]),float(row[1])
   xlist.append(x)
   ylist.append(y)
   plt.scatter(x,y)
  else:
   i=i+1
#
plt.plot(xlist,ylist, linestyle='solid', color='blue')
plt.show()
file.close()
