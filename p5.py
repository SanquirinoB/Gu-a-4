from vpython import *
import numpy as n

rRing=2
rE=0.1
m=5
m1=m
m2=2*m
g=9.8

t=n.linspace(0,10,1000)
dt = t[1]
#Angulo inicial
theta=pi/6
#Diferencia de angulo entre la esfera 1 y 2 dentro del anillo
dT=pi/4
#Radio para que las esferas no queden dentro del anillo
rPosE=rRing-2*rE
#Velocidad tangencial en base a la energía
v=n.sqrt((2/3)*g*rPosE*(2*n.sin(theta)+n.cos(theta)-1))
#Velocidad angular
omega=v/rPosE


#Definición de la posición inicial
ring=ring(pos=vector(0,0,0),axis=vector(0,0,1),radius=rRing,thickness=0.1)
e1=sphere(pos=vector(rPosE*n.cos(theta),-rPosE*n.sin(theta),0),radius=0.1,color=color.red)
e2=sphere(pos=vector(rPosE*n.sin(theta+dT),-rPosE*n.cos(theta+dT),0),radius=0.1,color=color.green)
stick=curve(pos=[e1.pos,e2.pos],color=vector(1,1,0.5))

#Movimiento
while True:
	for T in t:
		rate(100)
		theta_v=theta+v*T
		v_n=n.sqrt((2/3)*g*rPosE*(2*n.sin(theta_v)+n.cos(theta_v)-1))
		e1.pos=vector(rPosE*n.cos(theta_v),-rPosE*n.sin(theta_v),0)
		e2.pos=vector(rPosE*n.sin(dT+theta_v),-rPosE*n.cos(dT+theta_v),0)






