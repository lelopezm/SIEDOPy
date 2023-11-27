import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk, messagebox

# Definición de f(t,x) de x'=f(t,x)
def f(x, t, params):
    k = params[0]  # Asume que el primer parámetro es siempre k
    dxdt = k*x
    return dxdt

# Función que maneja la entrada del usuario y muestra los resultados
def solve_and_plot():
    try:
        # Obtiene los valores de los parámetros
        t0 = float(entry_t0.get())
        tf = float(entry_tf.get())
        x0 = float(entry_x0.get())
        params = [float(entry.get()) for entry in param_entries]

        # Asegura que t0 es menor que tf
        if t0 >= tf:
            messagebox.showerror("Error", "El tiempo inicial debe ser menor que el tiempo final.")
            return

        # Solución aproximada por el método de Euler
        T = np.linspace(t0, tf, 100)
        Sol = odeint(f, x0, T, args=(params,))
        X = Sol[:, 0]

        # Valor exacto y aproximado
        h = (tf - t0) / 100
        ve = x0 * np.exp(params[0] * (tf - t0))
        X_aprox = X[-1]
        E = abs(X_aprox - ve)

        # Mostrar resultados numéricos
        results_text.set(f'Valor exacto: x({tf})={ve:.6f}\n'
                         f'Valor aproximado: x({tf})={X_aprox:.6f}\n'
                         f'Error estimado: E={E:.12f} con un tamaño de paso h={h:.3f}')

        # Gráfica de la solución
        fig = plt.figure(figsize=(10, 6))
        plt.plot(T, X, '#12CFE1')
        plt.grid()
        plt.xlabel('t')
        plt.ylabel('x(t)')
        plt.title(f'Solución de $\dot{{x}}=ax$, $x({t0})=x_0$')

        # Colocar la gráfica en la interfaz gráfica
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")

# Funciones para agregar y remover parámetros
def add_param_field():
    entry = ttk.Entry(param_frame)
    entry.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)
    param_entries.append(entry)

def remove_param_field():
    if param_entries:
        entry = param_entries.pop()
        entry.destroy()

# Crear la ventana principal
window = tk.Tk()
window.title("Solución de Ecuaciones Diferenciales")

# Etiquetas y campos de entrada para tiempo inicial y condiciones iniciales
ttk.Label(window, text="Tiempo inicial (t0):").pack()
entry_t0 = ttk.Entry(window)
entry_t0.pack()

ttk.Label(window, text="Tiempo final (tf):").pack()
entry_tf = ttk.Entry(window)
entry_tf.pack()

ttk.Label(window, text="Condición inicial (x0):").pack()
entry_x0 = ttk.Entry(window)
entry_x0.pack()

# Marco para los parámetros adicionales
param_frame = ttk.LabelFrame(window, text="Parámetros")
param_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Lista para mantener los campos de entrada de los parámetros
param_entries = []

# Botones para agregar y remover parámetros
ttk.Button(param_frame, text="Agregar Parámetro", command=add_param_field).pack(side=tk.LEFT, padx=5, pady=5)
ttk.Button(param_frame, text="Remover Parámetro", command=remove_param_field).pack(side=tk.RIGHT, padx=5, pady=5)

# Botón para ejecutar la solución y mostrar la gráfica
solve_button = ttk.Button(window, text="Resolver y Graficar", command=solve_and_plot)
solve_button.pack()

# Etiqueta para mostrar resultados numéricos
results_text = tk.StringVar()
results_label = ttk.Label(window, textvariable=results_text)
results_label.pack()

# Iniciar el bucle principal de Tkinter
window.mainloop()
