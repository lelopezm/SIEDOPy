import funcionesODE as fode
import matplotlib.pyplot as plt
import numpy as np

#tiempo final y número de iteraciones 
tf=10
n=500
#condiciones iniciales
t0=0
x0=2
#parámetros
a=0.35

#Solución aproximada por el método de Euler
T, X_E = fode.Euler(t0,tf,n,a,x0)

#Solución aproximada por el método RK2
T, X_2 = fode.RK2(t0,tf,n,a,x0)

#Solución aproximada por el método RK4
T, X_4 = fode.RK4(t0,tf,n,a,x0)

#gráfica de la solución
plt.figure(figsize=(10, 6))
plt.plot(T,X_E,'#12CFE1',label='Euler')
plt.plot(T,X_2,'#229954',label='RK2')
plt.plot(T,X_4,'#C0392B',label='RK4')
plt.grid()
plt.legend()
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('Solución de $\dot{x}=ax$, $x(0)=x_0$')
plt.show()

#RESULTADOS NUMÉRICOS
h=(tf-t0)/n #tamaño de paso
ve=x0*np.exp(a*tf) #valor exacto de x(tf)
XE_aprox=X_E[n] #valor aproximado con Euler
EE=abs(ve-XE_aprox) #error con Euler
X2_aprox=X_2[n] #valor aproximado con RK2
E2=abs(ve-X2_aprox) #error con RK2
X4_aprox=X_4[n] #valor aproximado con RK4
E4=abs(ve-X4_aprox) #error con RK4
print('Valor exacto: x(%d)=%.6f'%(tf,ve))
print('Valor aproximado con Euler: x(%d)=%1.6f'%(tf,XE_aprox))
print('Error estimado con Euler: E=%1.3f con un tamaño de paso h=%1.3f'%(EE,h))
print('Valor aproximado con RK2: x(%d)=%1.6f'%(tf,X2_aprox))
print('Error estimado con RK2: E=%1.6f con un tamaño de paso h=%1.3f'%(E2,h))
print('Valor aproximado con RK4: x(%d)=%1.6f'%(tf,X4_aprox))
print('Error estimado con RK4: E=%1.12f con un tamaño de paso h=%1.3f'%(E4,h))