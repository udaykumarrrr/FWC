import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
from sympy import symbols, Eq, solve 
import math
#for equations
import sys                                          
sys.path.insert(0,'/sdcard/Download/matrices/CoordGeo')
#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using 
import subprocess
import shlex
#end if
print("A straight line L is perpendicular to line 5x-y=1.The area of the triangle formed by the line and coordinate axis is 5.find equation of line L")

#Input parameters
A = np.array(([5,-1]))
B = np.array(([1]))
e1 = np.array(([1,0]))
e2 = np.array(([0,1]))
n1 = A
c1 = B
#
#direction vector       
m1 = omat@n1
#print(m1)


#point on the line
x1=c1/(n1@e1)
A1=x1*e1
#Generating line
k1=-1
k2=2
x_AB = line_dir_pt(m1,A1,k1,k2)
#
##Plotting line
plt.plot(x_AB[0,:],x_AB[1,:])#,label='$Line')
#
b = symbols('b')
eqn = Eq(5*(b**2-0*b),10)
b = solve(eqn)
print(b)
#defining points
O = np.array(([0,0]))
M = np.array(([5*(e2.T@b),0]))
N = np.array(([0,(e2.T@b)]))
print(O,M,N)

#perpendicular line 
P = np.array(([0.2,1]))
Q = np.array(([b]))
e1 = np.array(([1,0]))
n2 = P
c2 = Q
x2 = np.abs(c2)/(n2@e1)
x2 = np.array(([x2.item(0),x2.item(1)]))
P1 = x2*e1
#print(P1)
m2 = omat@n2
k3 = -10
k4 = 10
x_PQ = line_dir_pt(m2,P1,k3,k4)

plt.plot(x_PQ[0,:],x_PQ[1,:])
#print(x_PQ)

#
tri_coords = np.vstack((M,N,O)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['M','N','O']
for i, txt in enumerate(vert_labels):
     plt.annotate(txt, # this is the text
                   (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                   textcoords="offset points", # how to position the text
                   xytext=(0,10), # distance from text to points (x,y)
                   ha='center') # horizontal alignment can be left, right or center


#
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
#plt.xlim(-5,10)
#plt.ylim(-5,10)

#for termux 
plt.savefig('/sdcard/Download/matrices/lines/line1.pdf')
subprocess.run(shlex.split("termux-open '/sdcard/Download/matrices/lines/line1.pdf'"))
#else
#plt.show()
