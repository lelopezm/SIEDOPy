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

# Crear la ventana principal
root = tk.Tk()
root.title("Menú de Aplicación de Interfaces")

style = ttk.Style(root)
style.configure('Button', font=('Helvetica', 12))
# Configurar tamaño de la ventana
root.geometry("300x200")

# Crear un botón que al hacer clic ejecute la interfaz Solución Metodos Numericos
interfaz_button = ttk.Button(root, text="Solución Metodos Numericos", command=run_euler_interface)
interfaz_button.pack(pady=20)

# Crear un botón que al hacer clic ejecute la interfaz de crecimiento exponencial
first_interface_button = ttk.Button(root, text="Interfaz de Crecimiento Exponencial", command=run_first_interface)
first_interface_button.pack(pady=10)

# Crear un botón que al hacer clic salga de la interfaz 
salir_button = ttk.Button(root, text="Salir", command=salir_de_la_aplicacion)
salir_button.pack(pady=20)

# Iniciar el bucle principal de Tkinter
root.mainloop()
