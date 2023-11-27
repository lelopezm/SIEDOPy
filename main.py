import subprocess
import os
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

# Lista para mantener un registro de los procesos abiertos
processes = []

def salir_de_la_aplicacion():
    # Termina todos los procesos antes de salir
    for process in processes:
        process.terminate()  # Intenta terminar el proceso
        process.wait()       # Espera a que el proceso se haya cerrado
    root.destroy()

def run_first_interface():
    try:
        # Ruta al script que deseas ejecutar
        script_path = os.path.join(sys.path[0], 'ScriptsPython', 'primero.py')
        
        # Verifica si el archivo existe antes de intentar ejecutarlo
        if os.path.isfile(script_path):
            # Ejecuta el script y guarda el proceso
            process = subprocess.Popen(['python', script_path])
            processes.append(process)  # Guarda la referencia al proceso
        else:
            messagebox.showerror("Error", "El archivo primero.py no se encontró.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Hubo un error al ejecutar primero.py: {e}")

def run_euler_interface():
    try:
        # Ruta al script que deseas ejecutar
        script_path = os.path.join(sys.path[0], 'ScriptsPython', 'CodigosPVI', 'InterfazODE.py')
        
        # Verifica si el archivo existe antes de intentar ejecutarlo
        if os.path.isfile(script_path):
            # Ejecuta el script y guarda el proceso
            process = subprocess.Popen(['python', script_path])
            processes.append(process)  # Guarda la referencia al proceso
        else:
            messagebox.showerror("Error", "El archivo InterfazODE.py no se encontró.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Hubo un error al ejecutar InterfazODE.py: {e}")

def run_modelo_exponencial_interface():
    try:
        # Ruta al script que deseas ejecutar
        script_path = os.path.join(sys.path[0], 'ScriptsPython', 'CodigosPVI', 'InterfazModeloExponencial.py')
        
        # Verifica si el archivo existe antes de intentar ejecutarlo
        if os.path.isfile(script_path):
            # Ejecuta el script y guarda el proceso
            process = subprocess.Popen(['python', script_path])
            processes.append(process)  # Guarda la referencia al proceso
        else:
            messagebox.showerror("Error", "El archivo InterfazModeloExponencial.py no se encontró.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Hubo un error al ejecutar InterfazModeloExponencial.py: {e}")

def run_modelo_newton_interface():
    try:
        # Ruta al script que deseas ejecutar
        script_path = os.path.join(sys.path[0], 'ScriptsPython', 'CodigosPVI', 'InterfazModeloNewton.py')
        
        # Verifica si el archivo existe antes de intentar ejecutarlo
        if os.path.isfile(script_path):
            # Ejecuta el script y guarda el proceso
            process = subprocess.Popen(['python', script_path])
            processes.append(process)  # Guarda la referencia al proceso
        else:
            messagebox.showerror("Error", "El archivo InterfazModeloNewton.py no se encontró.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Hubo un error al ejecutar InterfazModeloNewton.py: {e}")

# Configuración del estilo
def set_style():
    style = ttk.Style()
    style.configure('TButton', font=('Helvetica', 14), padding=6)
    style.configure('TLabel', font=('Helvetica', 14), padding=6)
    style.configure('TFrame', background='#e1e1e1')

# Crear la ventana principal
root = tk.Tk()
root.title("SIEDOPY")

set_style()

# Configurar tamaño de la ventana
root.geometry("400x300")  # Tamaño aumentado para dar más espacio

# Marco para los botones
button_frame = ttk.Frame(root, padding="10")
button_frame.pack(fill='both', expand=True)

# Configura las columnas del grid para que expandan y centren los botones
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

# Crear y colocar los botones en el marco usando un grid layout
interfaz_button = ttk.Button(button_frame, text="Metodos Numericos", command=run_euler_interface)
interfaz_button.grid(row=0, column=0, columnspan=3, sticky='ew', padx=10, pady=10)

first_interface_button = ttk.Button(button_frame, text="Crecimiento Exponencial", command=run_first_interface)
first_interface_button.grid(row=1, column=0, columnspan=3, sticky='ew', padx=10, pady=10)

modelo_exponencial_button = ttk.Button(button_frame, text="Modelo Exponencial", command=run_modelo_exponencial_interface)
modelo_exponencial_button.grid(row=2, column=0, columnspan=3, sticky='ew', padx=10, pady=10)

modelo_newton_button = ttk.Button(button_frame, text="Modelo de Newton", command=run_modelo_newton_interface)
modelo_newton_button.grid(row=3, column=0, columnspan=3, sticky='ew', padx=10, pady=10)

salir_button = ttk.Button(button_frame, text="Salir", command=salir_de_la_aplicacion)
salir_button.grid(row=4, column=0, columnspan=3, sticky='ew', padx=10, pady=10)

# Añadir un poco de espacio al final del grid para mejor estética
button_frame.grid_rowconfigure(5, weight=1)

# Iniciar el bucle principal de Tkinter
root.mainloop()
