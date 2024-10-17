import customtkinter as ctk
from matriz import Matriz
from escalar import Escalar
from documentacion import Documentacion

# Configuración de la ventana principal
ctk.set_appearance_mode("dark")  # Modo claro
ctk.set_default_color_theme("blue")  # Tema azul por defecto

root = ctk.CTk()  # Inicialización del objeto raíz
root.title("Calculadora de Multiplicación")
root.geometry("1080x720")

# Funciones para mostrar las opciones de matriz o escalar
def mostrar_matriz():
    escalar_app.frame.pack_forget()  # Ocultar interfaz de escalar
    documentacion_app.frame.pack_forget()  # Ocultar interfaz de documentación
    matriz_app.frame.pack(fill=ctk.BOTH, expand=True)  # Mostrar interfaz de matriz

def mostrar_escalar():
    matriz_app.frame.pack_forget()  # Ocultar interfaz de matriz
    documentacion_app.frame.pack_forget()  # Ocultar interfaz de documentación
    escalar_app.frame.pack(fill=ctk.BOTH, expand=True)  # Mostrar interfaz de escalar

def mostrar_documentacion():
    matriz_app.frame.pack_forget()  # Ocultar interfaz de matriz
    escalar_app.frame.pack_forget()  # Ocultar interfaz de escalar
    documentacion_app.frame.pack(fill=ctk.BOTH, expand=True)  # Mostrar interfaz de documentación

# Frame superior para opciones
frame_opciones = ctk.CTkFrame(root)
frame_opciones.pack(pady=10)

# Botones de opciones
btn_matriz = ctk.CTkButton(frame_opciones, text="Multiplicación de Matrices", command=mostrar_matriz)
btn_matriz.pack(side=ctk.LEFT, padx=5)

btn_escalar = ctk.CTkButton(frame_opciones, text="Multiplicación por Escalar", command=mostrar_escalar)
btn_escalar.pack(side=ctk.LEFT, padx=5)

btn_documentacion = ctk.CTkButton(frame_opciones, text="¿Cómo usar?", command=mostrar_documentacion)
btn_documentacion.pack(side=ctk.LEFT, padx=5)

# Frame donde se mostrará la interfaz de matriz o escalar
frame_contenido = ctk.CTkFrame(root)
frame_contenido.pack(pady=20)

# Instanciar las clases Matriz, Escalar y Documentacion
matriz_app = Matriz(frame_contenido)
escalar_app = Escalar(frame_contenido)
documentacion_app = Documentacion(frame_contenido)

# Mostrar la opción de matriz al inicio
mostrar_matriz()

# Iniciar el bucle principal de la interfaz
root.mainloop()
