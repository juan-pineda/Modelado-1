from time import sleep

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.cm as cm 
from matplotlib import animation 

#creamos las celulas


A=np.diag([1,2,3])
A
#cambiamos fila 3 por la fila 1 y bajamos 
np.roll(A,1,axis=0)
# posible dos posiciones  
np.roll(A,2,axis=0)
# una posicion ala izquierda
np.roll(A,-1,axis=0)
#posicion hacia otra casilla
np.roll(A,1,axis=1)

#definimos el vecindario 

def vecindario(A):
    vecindario = (
        np.roll(np.roll(A, 1, 1), 1, 0) +  # mueve arriba-izquierda
        np.roll(A, 1, 0) +  # Arriba
        np.roll(np.roll(A, -1, 1), 1, 0) +  # mueve arriba-derecha
        np.roll(A, -1, 1) +  # Derecha
        np.roll(np.roll(A, -1, 1), -1, 0) +  # mueve abajo-derecha
        np.roll(A, -1, 0) +  # Abajo
        np.roll(np.roll(A, 1, 1), -1, 0) +  # mueve abajo-izquierda
        np.roll(A, 1, 1)  # Izquierda
    )
    return vecindario 


   #definiremos que celulas mueren y nacen

#definimos un paso 
def paso(A):

 #calculamos el vecindario A
 #hacemos una copia de la matriz


    v = vecindario(A)  
    buffer_A = A.copy()
    for i in range(buffer_A.shape[0]):
        for j in range(buffer_A.shape[1]):
            if v[i, j] == 3 or (v[i, j] == 2 and buffer_A[i, j]):
                buffer_A[i, j] = 1
            else:
                buffer_A[i, j] = 0
    return buffer_A

    #parametros 
G=30   #G=generaciones permitidas
B=8
C=8

#la malla es

malla=np.zeros((B,C),dtype=int)    #matriz homogenea 
malla[1,1:4]=1
malla[2,1]=1
malla[3,2]=1

#creamos los imagenes 

fig=plt.figure(figsize=(5,5))
x=fig.add_subplot(111)    #cuadricula de 1x1 
x.axis('off')
A=malla
imagen=x.imshow(A,interpolation="none",cmap=cm.gray_r)

plt.savefig 

def animate(i):
     global A
     A=paso(A)
     imagen.set_data(A)
     anim=animation.FuncAnimation(fig, animate, frames=G,blit=true)
     anim.save('juego_vida_yeison.mp4',fps=10)
     
#representamos la animacion 
plt.ion()
fig=plt.figure()
x=fig.add_subplot(111)
A=malla
x.imshow(A,interpolation="none")
#tiempo o paso temporal
t=0.08 
for i in range(30):
    A=paso(A)
    x.imshow(A,interpolation="none")
    plt.draw()
    sleep(t)

def A():
    print"A"
if_name_=="_main_":
    A()
