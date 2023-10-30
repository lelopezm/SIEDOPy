import numpy as np

#función f(t,x) de la ODE x'=f(t,x)
def f(t,x,a):
    return a*x + 0*t

#Solución aproximada por el Método de Euler
def Euler(t0,tf,n,a,x0):
    h=(tf-t0)/n
    T=[t0]
    X=[x0]
    for i in range(n):
        T.append(T[-1]+h)
        X.append(X[-1]+h*f(T[-1],X[-1],a))
    return T, X 

#Solución aproximada por el Método de Runge-Kutta de segundo orden
def RK2(t0,tf,n,a,x0):
    h=(tf-t0)/n
    T=[t0]
    K1=[f(t0,x0,a)]
    K2=[f(t0+h,x0+h*K1[-1],a)]
    X=[x0]
    for i in range(n):
        T.append(T[-1]+h)
        K1.append(f(T[-1],X[-1],a))
        K2.append(f(T[-1]+h,X[-1]+h*K1[-1],a))
        X.append(X[-1]+h*(K1[-1]+K2[-1])/2)
    return T, X 

#Solución aproximada por el Método de Runge-Kutta de segundo orden
def RK4(t0,tf,n,a,x0):
    h=(tf-t0)/n
    T=[t0]
    K1=[f(t0,x0,a)]
    K2=[f(t0+h/2,x0+h*K1[-1]/2,a)]
    K3=[f(t0+h/2,x0+h*K2[-1]/2,a)]
    K4=[f(t0+h,x0+h*K3[-1],a)]
    X=[x0]
    for i in range(n):
        T.append(T[-1]+h)
        K1.append(f(T[-1],X[-1],a))
        K2.append(f(T[-1]+h/2,X[-1]+h*K1[-1]/2,a))
        K3.append(f(T[-1]+h/2,X[-1]+h*K2[-1]/2,a))
        K4.append(f(T[-1]+h,X[-1]+h*K3[-1],a))
        X.append(X[-1]+h*(K1[-1]+2*K2[-1]+2*K3[-1]+K4[-1])/6)
    return T, X 