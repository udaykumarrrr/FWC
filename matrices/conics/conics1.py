import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from sympy import symbols, Eq, solve 
import math
#for equations
import sys      
import sympy as sym
from sympy import Poly,roots,simplify
sys.path.insert(0,'/sdcard/Download/matrices/CoordGeo')
#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using 
import subprocess
import shlex
#end if
#
def hyper_gen(y):
    x= np.sqrt(9+y**2)
    return x
#
len = 20
y = np.linspace(-20,len)
x = hyper_gen(y)
plt.axhline(y=0,color='black')
plt.axvline(x=0,color= 'black')
#plotting the hyperbola
plt.plot(x,y,label='Hyperbola')
plt.plot(-x,y)

#
V = np.array(([1,0],[0,-1]))
u = np.array(([0,0]))
m2 = np.array(([0,1]))
q2 = np.array(([9,0]))
f = -9


d = np.sqrt((m2.T@(V@q2 + u))**2 - (q2.T@V@q2 + 2*u.T@q2 + f)*(m2.T@V@m2))
K1 = (d - m2.T@(V@q2 + u))/(m2.T@V@m2)
K2 = (-d - m2.T@(V@q2 + u))/(m2.T@V@m2)
print(K1)
print(K2)
a0 = q2 + K1*m2
a1 = q2 + K2*m2
print(a0)
print(a1)
x=sym.Symbol('x')
y=sym.Symbol('y')
X=np.array([x,y])
F0=np.transpose(V@np.transpose(a0)+np.transpose(u))@np.transpose(X) + u@np.transpose(a0) + f
F1=np.transpose(V@np.transpose(a1)+np.transpose(u))@np.transpose(X) + u@np.transpose(a1) + f
print(F0)
print(F1)
F = F0*F1
print(F)
#input line
n = np.array(([1,0]))
c = np.array(([9]))
e1 = np.array(([1,0]))
x0 = c/(n@e1)
A0 = x0*e1
m0 = omat@n


#plotting tangents
n1 = -(np.transpose(V@np.transpose(a0)+np.transpose(u)))
n2 = -(np.transpose(V@np.transpose(a1)+np.transpose(u)))
c1 = u@np.transpose(a0)+f
c2 = u@np.transpose(a1)+f
m1 = omat@n1
m2 = omat@n2
e1 = np.array(([0,1]))
x1 = c1/(n1@e1)
A1 = x1*e1
x2 = c2/(n2@e1)
A2 = x2*e1
k1 = -1
k2 = 3
k3 = -10
k4 = 10
#
x_nc =line_dir_pt(m0,A0,k3,k4)
plt.plot(x_nc[0,:],x_nc[1,:])

x_AB =line_dir_pt(m1,A1,k1,k2)
plt.plot(x_AB[0,:],x_AB[1,:])
x_CD =line_dir_pt(m2,A2,k1,k2)
plt.plot(x_CD[0,:],x_CD[1,:])

#
tri_coords = np.vstack((u,a0,a1)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['u','a0','a1']
for i, txt in enumerate(vert_labels):
     plt.annotate(txt, # this is the text
                   (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                   textcoords="offset points", # how to position the text
                   xytext=(0,10), # distance from text to points (x,y)
                   ha='center') # horizontal alignment can be left, right or center

#
#
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
#plt.xlim(-5,10)
#plt.ylim(-5,10)

#for termux 
plt.savefig('/sdcard/Download/matrices/conics/conics11.pdf')
subprocess.run(shlex.split("termux-open '/sdcard/Download/matrices/conics/conics11.pdf'"))
#else
#plt.show()
