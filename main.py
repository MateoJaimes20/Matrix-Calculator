import tkinter as tk
from tkinter import ttk
from matriz import Matriz
from escalar import Escalar
from documentacion import Documentacion


# Configuración de la ventana principal
root = tk.Tk()  # Inicialización del objeto raíz
root.title("Calculadora de Multiplicación")
root.geometry("1000x800")
root.configure(bg="#cccccc")  # Fondo de la aplicación

# Crear el estilo de ttk
style = ttk.Style(root)
style.theme_use("clam")
style.configure(
    "TButton", background="#39a0fc", foreground="white", font=("Helvetica", 10, "bold")
)
style.map("TButton", background=[("active", "#206098")])

# Funciones para mostrar las opciones de matriz o escalar
def mostrar_matriz():
    escalar_app.frame.pack_forget()  # Ocultar interfaz de escalar
    documentacion_app.frame.pack_forget()  # Ocultar interfaz de documentación
    matriz_app.frame.pack(fill=tk.BOTH, expand=True)  # Mostrar interfaz de matriz

def mostrar_escalar():
    matriz_app.frame.pack_forget()  # Ocultar interfaz de matriz
    documentacion_app.frame.pack_forget()  # Ocultar interfaz de documentación
    escalar_app.frame.pack(fill=tk.BOTH, expand=True)  # Mostrar interfaz de escalar

def mostrar_documentacion():
    matriz_app.frame.pack_forget()  # Ocultar interfaz de matriz
    escalar_app.frame.pack_forget()  # Ocultar interfaz de escalar
    documentacion_app.frame.pack(fill=tk.BOTH, expand=True)  # Mostrar interfaz de documentación

# Frame superior para opciones
frame_opciones = tk.Frame(root)
frame_opciones.pack(pady=10)

# Botones de opciones
btn_matriz = ttk.Button(
    frame_opciones, text="Multiplicación de Matrices", command=mostrar_matriz
)
btn_matriz.pack(side=tk.LEFT, padx=5)

btn_escalar = ttk.Button(
    frame_opciones, text="Multiplicación por Escalar", command=mostrar_escalar
)
btn_escalar.pack(side=tk.LEFT, padx=5)

btn_documentacion = ttk.Button(  # Cambié el nombre del botón a btn_documentacion
    frame_opciones, text="¿Cómo usar?", command=mostrar_documentacion
)
btn_documentacion.pack(side=tk.LEFT, padx=5)

# Frame donde se mostrará la interfaz de matriz o escalar
frame_contenido = tk.Frame(root)
frame_contenido.pack(pady=20)

# Instanciar las clases Matriz y Escalar
matriz_app = Matriz(frame_contenido)
escalar_app = Escalar(frame_contenido)
documentacion_app = Documentacion(frame_contenido)

# Mostrar la opción de matriz al inicio
mostrar_matriz()

# Iniciar el bucle principal de la interfaz
root.mainloop()
