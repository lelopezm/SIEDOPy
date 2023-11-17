import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import funcionesODE as fode

# Función para ejecutar los métodos de solución seleccionados y mostrar los resultados
def ejecutar_simulacion():
    # Obtiene los valores de entrada del usuario
    tf = float(entry_tf.get())
    n = int(entry_n.get())
    t0 = float(entry_t0.get())
    x0 = float(entry_x0.get())
    a = float(entry_a.get())
    
    # Calcula el tamaño de paso
    h = (tf - t0) / n
    
    # Obtiene el valor exacto para comparar con las aproximaciones
    ve = x0 * np.exp(a * tf)
    
    # Limpia la figura para los nuevos gráficos
    ax.clear()

    # Ejecución de los métodos seleccionados
    T = np.linspace(t0, tf, n+1)
    if var_euler.get():
        T, X_E = fode.Euler(t0, tf, n, a, x0)
        ax.plot(T, X_E, '#12CFE1', label='Euler')
        error_euler = abs(ve - X_E[-1])
        label_resultados['text'] += f'Euler: x({tf})={X_E[-1]:.6f}, Error={error_euler:.3e}\n'
    if var_rk2.get():
        T, X_2 = fode.RK2(t0, tf, n, a, x0)
        ax.plot(T, X_2, '#229954', label='RK2')
        error_rk2 = abs(ve - X_2[-1])
        label_resultados['text'] += f'RK2: x({tf})={X_2[-1]:.6f}, Error={error_rk2:.3e}\n'
    if var_rk4.get():
        T, X_4 = fode.RK4(t0, tf, n, a, x0)
        ax.plot(T, X_4, '#C0392B', label='RK4')
        error_rk4 = abs(ve - X_4[-1])
        label_resultados['text'] += f'RK4: x({tf})={X_4[-1]:.6f}, Error={error_rk4:.3e}\n'

    # Actualiza la gráfica
    ax.legend()
    ax.set_xlabel('t')
    ax.set_ylabel('x(t)')
    ax.set_title('Solución de dx/dt = ax, x(0) = x0')
    canvas.draw()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Simulador de Métodos Numéricos para ODEs")

# Definición de los campos de entrada y etiquetas
label_tf = tk.Label(root, text="Tiempo final (tf):")
label_n = tk.Label(root, text="Número de iteraciones (n):")
label_t0 = tk.Label(root, text="Tiempo inicial (t0):")
label_x0 = tk.Label(root, text="Condición inicial (x0):")
label_a = tk.Label(root, text="Parámetro (a):")
entry_tf = tk.Entry(root)
entry_n = tk.Entry(root)
entry_t0 = tk.Entry(root)
entry_x0 = tk.Entry(root)
entry_a = tk.Entry(root)

# Inicialización de las entradas con valores por defecto
entry_tf.insert(0, '10')
entry_n.insert(0, '5')
entry_t0.insert(0, '0')
entry_x0.insert(0, '2')
entry_a.insert(0, '0.35')

# Checkboxes para selección de métodos
var_euler = tk.BooleanVar(value=True)
check_euler = tk.Checkbutton(root, text="Método de Euler", variable=var_euler)
var_rk2 = tk.BooleanVar(value=True)
check_rk2 = tk.Checkbutton(root, text="Método RK2", variable=var_rk2)
var_rk4 = tk.BooleanVar(value=True)
check_rk4 = tk.Checkbutton(root, text="Método RK4", variable=var_rk4)

# Botón para ejecutar la simulación
button_run = tk.Button(root, text="Ejecutar Simulación", command=ejecutar_simulacion)

# Configuración del área de gráficos
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Área de resultados
label_resultados = tk.Label(root, text='', justify=tk.LEFT)
label_resultados.pack(side=tk.BOTTOM, fill=tk.X)

# Empaquetado de los widgets en la ventana
label_tf.pack()
entry_tf.pack()
label_n.pack()
entry_n.pack()
label_t0.pack()
entry_t0.pack()
label_x0.pack()
entry_x0.pack()
label_a.pack()
entry_a.pack()
check_euler.pack()
check_rk2.pack()
check_rk4.pack()
button_run.pack()

# Bucle principal de la aplicación
root.mainloop()
