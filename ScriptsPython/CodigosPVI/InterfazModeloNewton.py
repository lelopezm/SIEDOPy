import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk, messagebox

# Definición de f(x,t,k,Ta) de x'=f(x,t,k,Ta)
def f(x, t, k, Ta):
    dxdt = k * x * (x - Ta)
    return dxdt

# Función que maneja la entrada del usuario y muestra los resultados
def solve_and_plot():
    try:
        # Obtiene los valores de los parámetros
        k = float(entry_k.get())
        Ta = float(entry_Ta.get())
        t0 = float(entry_t0.get())
        tf = float(entry_tf.get())
        x0 = float(entry_x0.get())

        # Asegura que t0 es menor que tf
        if t0 >= tf:
            messagebox.showerror("Error", "El tiempo inicial debe ser menor que el tiempo final.")
            return

        # Solución aproximada por el método de Euler
        T = np.linspace(t0, tf, 100)
        Sol = odeint(f, x0, T, args=(k, Ta))
        X = Sol[:, 0]

        # Valor aproximado
        X_aprox = X[-1]

        # Mostrar resultados numéricos
        results_text.set(f'Valor aproximado: x({tf})={X_aprox:.6f}')

        # Gráfica de la solución
        fig = plt.figure(figsize=(10, 6))
        plt.plot(T, X, '#12CFE1')
        plt.grid()
        plt.xlabel('t')
        plt.ylabel('x(t)')
        plt.title('Solución de la ecuación diferencial')

        # Colocar la gráfica en la interfaz gráfica
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")

# Crear la ventana principal
window = tk.Tk()
window.title("Simulador de Ecuación Diferencial")

# Etiquetas y campos de entrada para parámetros y condiciones iniciales
ttk.Label(window, text="Parámetro k:").pack()
entry_k = ttk.Entry(window)
entry_k.pack()

ttk.Label(window, text="Temperatura ambiente Ta:").pack()
entry_Ta = ttk.Entry(window)
entry_Ta.pack()

ttk.Label(window, text="Tiempo inicial (t0):").pack()
entry_t0 = ttk.Entry(window)
entry_t0.pack()

ttk.Label(window, text="Tiempo final (tf):").pack()
entry_tf = ttk.Entry(window)
entry_tf.pack()

ttk.Label(window, text="Condición inicial (x0):").pack()
entry_x0 = ttk.Entry(window)
entry_x0.pack()

# Botón para ejecutar la solución y mostrar la gráfica
solve_button = ttk.Button(window, text="Resolver y Graficar", command=solve_and_plot)
solve_button.pack()

# Etiqueta para mostrar resultados numéricos
results_text = tk.StringVar()
results_label = ttk.Label(window, textvariable=results_text)
results_label.pack()

# Iniciar el bucle principal de Tkinter
window.mainloop()
