import subprocess
import os
import sys
import tkinter as tk
from tkinter import messagebox

def run_euler_interface():
    try:
        # Ruta al script que deseas ejecutar
        script_path = os.path.join(sys.path[0], 'ScriptsPython', 'CodigosPVI', 'InterfazODE.py')
        
        # Verifica si el archivo existe antes de intentar ejecutarlo
        if os.path.isfile(script_path):
            # Ejecuta el script
            subprocess.run(['python', script_path], check=True)
        else:
            messagebox.showerror("Error", "El archivo InterfazODE.py no se encontró.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Hubo un error al ejecutar InterfazODE.py: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Menú de Aplicación de Interfaces")

# Configurar tamaño de la ventana
root.geometry("300x200")

# Crear un botón que al hacer clic ejecute la interfaz Euler
euler_button = tk.Button(root, text="Euler", command=run_euler_interface)
euler_button.pack(pady=20)

# Iniciar el bucle principal de Tkinter
root.mainloop()
