import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import funcionesODE as fode

# Función para ejecutar los métodos de solución seleccionados y mostrar los resultados
def ejecutar_simulacion():
    label_resultados.config(text='')  # Limpiar resultados previos
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
        label_resultados.config(text=label_resultados.cget("text") + f'Euler: x({tf})={X_E[-1]:.6f}, Error={error_euler:.3e}\n')
    if var_rk2.get():
        T, X_2 = fode.RK2(t0, tf, n, a, x0)
        ax.plot(T, X_2, '#229954', label='RK2')
        error_rk2 = abs(ve - X_2[-1])
        label_resultados.config(text=label_resultados.cget("text") + f'RK2: x({tf})={X_2[-1]:.6f}, Error={error_rk2:.3e}\n')
    if var_rk4.get():
        T, X_4 = fode.RK4(t0, tf, n, a, x0)
        ax.plot(T, X_4, '#C0392B', label='RK4')
        error_rk4 = abs(ve - X_4[-1])
        label_resultados.config(text=label_resultados.cget("text") + f'RK4: x({tf})={X_4[-1]:.6f}, Error={error_rk4:.3e}\n')

    # Actualiza la gráfica
    ax.legend()
    ax.set_xlabel('t')
    ax.set_ylabel('x(t)')
    ax.set_title('Solución de dx/dt = ax, x(0) = x0')
    canvas.draw()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Simulador de Métodos Numéricos para ODEs")

# Configurar el estilo de ttk
style = ttk.Style(root)
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TEntry', font=('Helvetica', 12), padding=5)
style.configure('TButton', font=('Helvetica', 12), padding=5)
style.configure('TCheckbutton', font=('Helvetica', 12), padding=5)

# Contenedor principal
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Frame para los controles de entrada
controls_frame = ttk.LabelFrame(main_frame, text="Parámetros", padding="10")
controls_frame.pack(fill=tk.X)

# Frame para los resultados y el botón de ejecución
results_frame = ttk.Frame(main_frame, padding="10")
results_frame.pack(fill=tk.X, pady=10)

# Frame para el área de gráficos
graph_frame = ttk.Frame(root, padding="10")
graph_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Campos de entrada
label_tf = ttk.Label(controls_frame, text="Tiempo final (tf):")
label_n = ttk.Label(controls_frame, text="Número de iteraciones (n):")
label_t0 = ttk.Label(controls_frame, text="Tiempo inicial (t0):")
label_x0 = ttk.Label(controls_frame, text="Condición inicial (x0):")
label_a = ttk.Label(controls_frame, text="Parámetro (a):")
entry_tf = ttk.Entry(controls_frame)
entry_n = ttk.Entry(controls_frame)
entry_t0 = ttk.Entry(controls_frame)
entry_x0 = ttk.Entry(controls_frame)
entry_a = ttk.Entry(controls_frame)

# Organización de los campos de entrada en el grid
for i, (label, entry) in enumerate(((label_tf, entry_tf), (label_n, entry_n), (label_t0, entry_t0), 
                                     (label_x0, entry_x0), (label_a, entry_a))):
    label.grid(row=i, column=0, sticky="ew", padx=5, pady=5)
    entry.grid(row=i, column=1, sticky="ew", padx=5, pady=5)
    controls_frame.grid_columnconfigure(1, weight=1)

# Checkboxes para la selección de métodos
var_euler = tk.BooleanVar(value=True)
check_euler = ttk.Checkbutton(controls_frame, text="Método de Euler", variable=var_euler)
var_rk2 = tk.BooleanVar(value=True)
check_rk2 = ttk.Checkbutton(controls_frame, text="Método RK2", variable=var_rk2)
var_rk4 = tk.BooleanVar(value=True)
check_rk4 = ttk.Checkbutton(controls_frame, text="Método RK4", variable=var_rk4)
check_euler.grid(row=5, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
check_rk2.grid(row=6, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
check_rk4.grid(row=7, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

# Botón para ejecutar la simulación y etiqueta de resultados
button_run = ttk.Button(results_frame, text="Ejecutar Simulación", command=ejecutar_simulacion)
button_run.pack(side=tk.LEFT, padx=5, pady=5)
label_resultados = ttk.Label(results_frame, text='', font=('Helvetica', 12), justify=tk.LEFT)
label_resultados.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Configuración del área de gráficos
fig, ax = plt.subplots(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Bucle principal de la aplicación
root.mainloop()
