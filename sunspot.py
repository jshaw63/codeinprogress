import matplotlib.pyplot as plt

def readdata(document, column):
  file=open(document,"r")
  lines=file.readlines()
  file.close()
  data=[]
  for line in lines:
    p=line.split()
    data.append(p[column])
  return data

document="sunspotnumbers.txt"
xlist=readdata(document,0)
ylist=readdata(document,1)

plt.plot(xlist,ylist, linestyle='solid', color='blue')
plt.show()
