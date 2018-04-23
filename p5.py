from vpython import *
import numpy as n

rRing=2
rE=0.1
#Angulo inicial
theta=0
#Diferencia de angulo entre la esfera 1 y 2 dentro del anillo
dT=pi/4
#Radio para que las esferas no queden dentro del anillo
rPosE=rRing-2*rE


ring=ring(pos=vector(0,0,0),axis=vector(0,0,1),radius=rRing,thickness=0.1)
e1=sphere(pos=vector(rPosE*n.cos(theta),-rPosE*n.sin(theta),0),radius=0.1,color=color.red)
e2=sphere(pos=vector(rPosE*n.sin(theta+dT),-rPosE*n.cos(theta+dT),0),radius=0.1,color=color.green)
stick=curve(pos=[e1.pos,e2.pos],color=vector(1,1,0.5))


