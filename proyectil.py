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
ya = numpy.zeros(int((N/10)+1))

for i in range(0,1,1):
    xs[i]=0.0
tr=theta*pi/180.
vs[0]=v0*cos(tr)
vs[1]=v0*sin(tr)
i=0
e=energy(xs,vs,sdt,g)
fout1.write('%f\t%f\t%f\t%f\t%f\n' % (sdt,xs[0],xs[1],vs[0],vs[1]))
fout2.write('%f\t%f\t%f\t%f\n' % (sdt,e[0],e[1],e[2]))
D=(2.*(v0**2)*cos(tr)*sin(tr)/g)
H=((v0 * sin(tr))**2)/(2.*g)

j=0
xa[0]=xs[0]
ya[0]=xs[1]
#------------------Loop--------------------------------------
while (sdt < T):
    xs,vs=verlet(xs,vs,sdt,g,ga)
    sdt=sdt+(tstep)
    i=i+1
    if ((xs[1]<h_m)&(xs[1]>0.0)&(xs[0]>(d_m-a_m))&(xs[0]<(d_m+a_m))):
        vs[0]=-vs[0]
    elif xs[1]<=0:
        vs[1]=-vs[1]
    elif xs[0]<=0:
        vs[0]=-vs[0]
    elif xs[0]>=D:
        vs[0]=-vs[0]
    elif xs[1]>=(H+5.0):
        vs[1]=-vs[1]
    else:
        pass
    if (i==10):
        j=j+1
        xa[j]=xs[0]
        ya[j]=xs[1]
        e=energy(xs,vs,sdt,g)
        fout1.write('%f\t%f\t%f\t%f\t%f\n' % (sdt,xs[0],xs[1],vs[0],vs[1]))
        fout2.write('%f\t%f\t%f\t%f\n' % (sdt,e[0],e[1],e[2]))

        i=0
    else:
        pass
#----------------------------------------------------------------
D=((v0**2)*cos(tr)*sin(tr)/g)
H=((v0 * sin(tr))**2)/(2.*g)
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(autoscale_on=False, xlim=(0, 2.*D), ylim=(-10, H+5.))
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
trace, = ax.plot([], [], '.-', lw=1, ms=1)
wall, = ax.plot([], [], '.-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)             
plt.grid(True)
plt.title("Movimiento en 2 dimensiones: Proyectiles")
plt.xlabel("Coordenada x")
plt.ylabel("Coordenada y")



def animate(i):
    thisx = [xa[i]]
    thisy = [ya[i]]
    wallx = [[d_m,d_m]]
    wally = [[0,h_m]]
    history_x = xa[:i]
    history_y = ya[:i]

    line.set_data(thisx, thisy)
    trace.set_data(history_x, history_y)
    wall.set_data(wallx,wally)
    time_text.set_text(time_template % ((i*10)*dt))
    return line, wall, trace, time_text

ani = animation.FuncAnimation(fig, animate, len(xa), interval=dt*10, blit=False)
fout1.close()
fout2.close()


plt.figure(figsize=(4, 3), dpi=100)
plt.text(0.1,1.0,r'Coordenadas del vector r:',fontsize=11)
plt.text(0.1,0.9,r' x (MRU): $x(t)=x_0+v_0 \cos(\theta) t$',fontsize=11)
plt.text(0.1,0.8,r' y (MRUV): $y(t)=y_0+v_0 \sin(\theta) t-\frac{g t^2}{2}$',fontsize=11)
plt.text(0.1,0.7,r'Coordenadas del vector v:',fontsize=11)
plt.text(0.1,0.6,r'$v_x(t)=v_0 \cos(\theta) $',fontsize=11)
plt.text(0.1,0.5,r'$v_y(t)=v_0 \sin(\theta) - g t$',fontsize=11)

plt.axis('off')
plt.show()
                                                                                                                                                                                                                                                                                                         104,9         65%

