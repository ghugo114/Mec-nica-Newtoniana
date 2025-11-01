import sys, numpy,math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from numpy import *
#---------------------------------------------------------------
#----------Parametros-------------------------------------------
tstep=0.005
dt=tstep
pi=2.0*arcsin(1.0)
sdt=0.0
#--------------- Funcion Fuerza---------------------------------
def f(xs,vs,t,g,ga):

    fx=-ga*vs[0]
    fy=-g-(ga*vs[1])
    return fx,fy
#--------------------------------------------------------------
def euler(x,v,t,w02,g,a,w):
    v_h=v+(f(x,v,t,w02,g,a,w)*(tstep))
    x_h=x+v*(tstep)
    return x_h,v_h
#---------------------------------------------------------------
def verlet(xs,vs,t,g,ga):
    ax,ay=f(xs,vs,t,g,ga)
    xs[0]=xs[0]+(vs[0]*tstep)+(ax*(tstep**2)/2.)
    xs[1]=xs[1]+(vs[1]*tstep)+(ay*(tstep**2)/2.)
    #a_=a
    ax_,ay_=f(xs,vs,t,g,ga)
    vs[0]=vs[0]+((ax+ax_)*tstep/2.)
    vs[1]=vs[1]+((ay+ay_)*tstep/2.)
    return xs,vs
#--------------------------------------------------------------------
def energy(xs,vs,t,g):
    ep=g*xs[1]
    ec=(vs[0]**2+vs[1]**2)/2.
    em=ep+ec
    return ep,ec,em
#--------------------------------------------------------------------
#if len(sys.argv) < 6:
 #   sys.exit("Usage: python3 proyectil.py g gamma theta v0 T")
#coef = input("Ingrese g,gamma,angulo,velocidad,tmax: ej 9.8,0.1,45.0,23.0,10.0 \n").split(',')
#coef = numpy.array([float(a) for a in coef])
#muro = input("Ingrese distancia a la que se encuentra y altura del obstaculo: ej 10.0,5.0 (a 10 m de dist, 5 m altura)\n").split(',')
#muro = numpy.array([float(b) for b in muro])
print("Movimiento en dos dimensiones: Proyectiles bajo efecto de la gravedad\n")
print("con efecto de rozamiento con el aire, donde F es proporcional a velocidad\n")
print("y de signo opuesto cuyo modulo se calcula F_roz= -ga v, siendo F_roz y v vectores\n")
print("A continuacion ingrese g, ga (0 para no rozamiento), angulo inicial, velocidad inicial,\n")
print("y tiempo total cuando lea: Ingrese g,gamma,angulo,velocidad,tmax: ej 9.8,0.1,45.0,23.0,10.0 \n")
print("Luego ingrese la distancia a la que se encuentra un obstaculo y su altura\n")
print("Apareceran dos ventanas, una con el movimiento y trayectoria del proyectil\n")
print("Otra con las ecuaciones de movimiento para el caso sin rozamiento\n")
print("Programa desarrollado por Lic. Gastón Hugo, clases particulares de Física y Matemática\n")
print("Celular: 099750940\n")
print("Email: gaston.hugo@gmail.com\n")
print("Material disponible en https://gastonhugo.wixsite.com/cursos\n")
#------------------Comienza el programa--------------------------------
print("\n")
print("Comienza el programa que simula el movimiento de un proyectil con\n")
print("agregado de un obstaculo contra el que el objeto rebota si se encuentra con el\n")
coef = input("Ingrese g,gamma,angulo,velocidad,tmax: ej 9.8,0.1,45.0,23.0,10.0 \n").split(',')
coef = numpy.array([float(a) for a in coef])
muro = input("Ingrese distancia a la que se encuentra y altura del obstaculo: ej 10.0,5.0 (a 10 m de dist, 5 m altura)\n").split(',')
muro = numpy.array([float(b) for b in muro])


g=coef[0]#float(sys.argv[1])
ga=coef[1]#float(sys.argv[2])
theta=coef[2]#float(sys.argv[3])
v0=coef[3]#float(sys.argv[4])
T=coef[4]#float(sys.argv[5])
N=int(T/tstep)
#fpar=open('param_in.dat','w')
fout1=open('datos.dat','w')
fout2=open('energ.dat','w')

h_m=muro[1]#5.
d_m=muro[0]#10.
a_m=0.05
xs=numpy.zeros(2)
vs=numpy.zeros(2)
e=numpy.zeros(3)
xa = numpy.zeros(int((N/10)+1))
                                                                                                                                                                                                                                                                                                                             46,9     Comienzo

