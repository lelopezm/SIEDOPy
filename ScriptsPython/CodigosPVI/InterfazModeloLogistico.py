import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import *

# Definición de la función del sistema
def f(x, t, k, N):
    dxdt = k * x * (N - x)
    return dxdt

# Función para iniciar la simulación
def iniciar_simulacion():
    t0 = float(t0_entry.get())
    tf = float(tf_entry.get())
    x0 = float(x0_entry.get())
    k = float(k_entry.get())
    N = float(N_entry.get())

    T = np.linspace(t0, tf, 100)
    Sol = odeint(f, x0, T, args=(k, N))
    X = Sol[:, 0]

    # Gráfica de la solución
    fig = plt.figure(figsize=(10, 6))
    plt.plot(T, X, '#12CFE1')
    plt.grid()
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.title('Solución de la ecuación diferencial')

    # Mostrar gráfica en la interfaz
    canvas = FigureCanvasTkAgg(fig, master=window)  
    canvas.draw()
    canvas.get_tk_widget().pack()

    # RESULTADOS NUMÉRICOS
    X_aprox = X[-1]
    resultado_label.config(text='Valor aproximado: x(%d)=%1.6f' % (tf, X_aprox))

# Creación de la ventana principal
window = tk.Tk()
window.title("Simulación de ODE")

# Campos para parámetros
t0_label = tk.Label(window, text="Tiempo inicial (t0):")
t0_label.pack()
t0_entry = tk.Entry(window)
t0_entry.pack()

tf_label = tk.Label(window, text="Tiempo final (tf):")
tf_label.pack()
tf_entry = tk.Entry(window)
tf_entry.pack()

x0_label = tk.Label(window, text="Condición inicial (x0):")
x0_label.pack()
x0_entry = tk.Entry(window)
x0_entry.pack()

k_label = tk.Label(window, text="Tasa de crecimiento (k):")
k_label.pack()
k_entry = tk.Entry(window)
k_entry.pack()

N_label = tk.Label(window, text="Capacidad de carga (N):")
N_label.pack()
N_entry = tk.Entry(window)
N_entry.pack()

# Botón para iniciar simulación
iniciar_button = tk.Button(window, text="Iniciar Simulación", command=iniciar_simulacion)
iniciar_button.pack()

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(window, text="")
resultado_label.pack()

# Bucle principal de Tkinter
window.mainloop()
