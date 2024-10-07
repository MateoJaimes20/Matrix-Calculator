import tkinter as tk
from tkinter import font
from matriz import Matriz
from escalar import Escalar

class Aplicacion:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora de Multiplicación")
        self.master.geometry("1920x1080")

        # Definir la fuente Montserrat
        self.montserrat = font.Font(family="Montserrat", size=10)

        # Frame superior para opciones
        self.frame_opciones = tk.Frame(self.master)
        self.frame_opciones.pack(pady=10)

        self.btn_matriz = tk.Button(self.frame_opciones, text="Multiplicación de Matrices", command=self.mostrar_matriz, font=self.montserrat)
        self.btn_matriz.pack(side=tk.LEFT, padx=5)

        self.btn_escalar = tk.Button(self.frame_opciones, text="Multiplicación por Escalar", command=self.mostrar_escalar, font=self.montserrat)
        self.btn_escalar.pack(side=tk.LEFT, padx=5)

        # Frame donde se mostrará la interfaz de matriz o escalar
        self.frame_contenido = tk.Frame(self.master)
        self.frame_contenido.pack(pady=10)

        self.matriz_app = Matriz(self.frame_contenido)
        self.escalar_app = Escalar(self.frame_contenido)

        self.mostrar_matriz()  # Mostrar la opción de matriz al inicio

    def mostrar_matriz(self):
        self.escalar_app.frame.pack_forget()  # Ocultar escalar
        self.matriz_app.frame.pack(fill=tk.BOTH, expand=True)  # Mostrar matriz

    def mostrar_escalar(self):
        self.matriz_app.frame.pack_forget()  # Ocultar matriz
        self.escalar_app.frame.pack(fill=tk.BOTH, expand=True)  # Mostrar escalar

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
