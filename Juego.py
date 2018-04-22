from vpython import *
import numpy as np 

r = 5
omega = 5
t = np.linspace(0,10,1001)
dt = t[1]
v_z = 0

e1=sphere(pos=vector(r,0,0), radius=0.2,color=color.white,make_trial= True, interval=1)
e2=sphere(pos=vector(0,r,0), radius=0.2,color=color.red,make_trial= True, interval=1)
e3=sphere(pos=vector(0,0,r), radius=0.2,color=color.orange,make_trial= True, interval=1)

scene.autoscale = True

x_axis = arrow(pos=vector(0,0,0), axis=vector(1,0,0), color=color.red, shaftwidth=0.05)
y_axis = arrow(pos=vector(0,0,0), axis=vector(0,1,0), color=color.blue, shaftwidth=0.05)
z_axis = arrow(pos=vector(0,0,0), axis=vector(0,0,1), color=color.green, shaftwidth=0.05)

while True:
	for this_t in t:
		rate(60)
		alpha= omega*this_t
		e1.pos = vector(r*np.sin(theta),r*np.cos(theta),0)
		e2.pos = vector(r*np.sin(theta),0,r*np.cos(theta))
		e3.pos = vector(0,r*np.sin(theta),r*np.cos(theta))