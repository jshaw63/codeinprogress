# program filein
# j. shaw		3/16/17
#
# simple file input program to read x,y data from file
# 
# import libraries
#
import matplotlib.pyplot as plt
#
#  open file as in_file, then read lines
#  from the file and store whole file in 
#  "lines".  
#
in_file=open("input.txt","r")
lines=in_file.readlines()
in_file.close()
#
# this isn't absolutely necessary, but it will echo back 
# the number of lines in the file and store that number
#
num_lines = sum(1 for line in open('input.txt'))
print 'number of lines read =', num_lines
#
# the file content in a line of lines has to be split
# to get the x and y parts separately. We store the
# x's and y's in appendable lists. 0 is first item,x, and
# 1 the second item,y, in the line since python indices
# start with 0.  We convert strings to floats to be safe.
#
xlist,ylist = [],[]
for line in lines:
    p = line.split()
    x,y=float(p[0]),float(p[1])
    plt.scatter(x,y)
    xlist.append(x)
    ylist.append(y)
#
# plot, unlike scatter takes lists as arguments. If we 
# only use scatter(x,y) then the plot will be points
# without connecting lines.  If we call plot after
# scatter(x,y) then the plot(xlist,ylist) will put lines
# through the points.
#
plt.plot(xlist,ylist, linestyle='solid', color='blue')
plt.show()

