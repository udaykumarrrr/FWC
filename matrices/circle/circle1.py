#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0,'/sdcard/Download/matrices/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if

#Input parameters
r1 = 3       #radius   #distance of points from center
u1 = np.array(([0,0]))   #center
r2 = 4
u2 = np.array(([7,0]))
r3 = 5
u3 = np.array(([2.28571428571,7.66651878]))

e1 = np.array(([1,0]))

###Generating the circle
x_circ1= circ_gen(u1,r1)
x_circ2= circ_gen(u2,r2)
x_circ3= circ_gen(u3,r3)


#tangents
D = np.array(([4.57142857142,15.33303756],[9.42857142858,-15.3333756]))
d = np.array(([47.99999,-5.99999]))
e1 = np.array(([1,0]))
n1 = D[0,:]
n2 = D[1,:]
c1 = d[0]
c2 = d[1]
#
P =  LA.solve(D,d)
print(P)

m = u2-u1
m1 = omat@n1
m2 = omat@n2
#
x1 = c1/(n1@e1)
x2 = c2/(n2@e1)
D1 = x1*e1
E1 = x2*e1


k1 = -1
k2 = 1
k3 =-1
k4 = 1
#foot of perpendicular
z=m.T@(P-u1)
y=LA.norm(m)**2
G = u1+(z/y)*m
print(G)
#Distance
K1 = LA.norm(P-G)
print(K1)

#
x_PG = line_gen(P,G)
plt.plot(x_PG[0,:],x_PG[1,:])



##Plotting all lines
x_Dd = line_dir_pt(m1,D1,k1,k2)
x_Ee = line_dir_pt(m2,E1,k1,k2)
#
plt.plot(x_Dd[0,:],x_Dd[1,:],label='$line$')
plt.plot(x_Ee[0,:],x_Ee[1,:])
#
#
#Plotting the circle
plt.plot(x_circ1[0,:],x_circ1[1,:],label='$Circle$')
plt.plot(x_circ2[0,:],x_circ2[1,:],label='$Circle$')
plt.plot(x_circ3[0,:],x_circ3[1,:],label='$Circle$')
#Labeling the coordinates
tri_coords = np.vstack((u1,u2,u3,P,G)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['u1','u2','u3','P','G']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-5,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('/sdcard/Download/matrices/Circle/circle1.pdf')
subprocess.run(shlex.split("termux-open '/sdcard/Download/matrices/Circle/circle1.pdf'"))
#else
#plt.show()
