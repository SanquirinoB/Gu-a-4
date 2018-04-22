from vpython import *
import numpy as np 

r = 5
omega = 5
t = np.linspace(0,10,1001)
dt = t[1]
v_z = 0

e1=sphere(pos=vector(r,0,0), radius=2,color=color.white,make_trial= True, interval=1)
e2=sphere(pos=vector(0,r,0), radius=2,color=color.red,make_trial= True, interval=1)
e3=sphere(pos=vector(0,0,r), radius=2,color=color.orange,make_trial= True, interval=1)

a1=arrow(pos=e1.pos,axis=e2.pos-e1.pos,color=color.green)
a2=arrow(pos=e2.pos,axis=e3.pos-e2.pos,color=color.yellow)
a3=arrow(pos=e3.pos,axis=e1.pos-e3.pos,color=color.cyan)

scene.autoscale = True

x_axis = arrow(pos=vector(0,0,0), axis=vector(1,0,0), color=color.red, shaftwidth=0.05)
y_axis = arrow(pos=vector(0,0,0), axis=vector(0,1,0), color=color.blue, shaftwidth=0.05)
z_axis = arrow(pos=vector(0,0,0), axis=vector(0,0,1), color=color.green, shaftwidth=0.05)

while True:
	for this_t in t:
		rate(60)
		theta = omega*this_t
		a1.axis = a2.axis = a3.axis = vector(np.cos(theta),np.sin(theta),0)
		e1.pos =e2.pos = e3.pos = vector(r*np.cos(theta), r*np.sin(theta),
			v_z*this_t)