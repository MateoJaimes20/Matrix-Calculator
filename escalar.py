import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import numpy as np

def multiplicar_matriz_por_escalar(matriz, escalar):
    return [[round(elemento * escalar, 4) for elemento in fila] for fila in matriz]

def obtener_matriz(entries, rows, cols):
    matriz = []
    try:
        for i in range(rows):
            fila = []
            for j in range(cols):
                valor = float(entries[i][j].get())
                fila.append(valor)
            matriz.append(fila)
    except ValueError:
        messagebox.showerror("Error", "Todos los valores deben ser números.")
        return None
    return matriz

class Escalar:
    def __init__(self, master):
        self.frame = ctk.CTkFrame(master)
        self.crear_widgets()
        self.resultados_frame = ctk.CTkFrame(self.frame)
        self.resultados_frame.grid(row=8, columnspan=4, pady=5)
        self.resultados_adicionales = []  

    def crear_widgets(self):
        self.tamano_A_label = ctk.CTkLabel(self.frame, text="Tamaño de la matriz A (Filas x Columnas):")
        self.tamano_A_label.grid(row=0, column=0, padx=5, pady=5)

        self.filas_A_entry = ctk.CTkEntry(self.frame, width=50)
        self.filas_A_entry.grid(row=0, column=1, padx=(0, 2), pady=5)

        self.x_label = ctk.CTkLabel(self.frame, text="x")
        self.x_label.grid(row=0, column=2, padx=2, pady=5)

        self.cols_A_entry = ctk.CTkEntry(self.frame, width=50)
        self.cols_A_entry.grid(row=0, column=3, padx=(2, 0), pady=5)

        self.escalar_label = ctk.CTkLabel(self.frame, text="Escalar:")
        self.escalar_label.grid(row=1, column=0, padx=5, pady=5)

        self.escalar_entry = ctk.CTkEntry(self.frame, width=50)
        self.escalar_entry.grid(row=1, column=1, padx=(0, 2), pady=5)

        self.boton_generar = ctk.CTkButton(self.frame, text="Generar Entradas", command=self.generar_entradas)
        self.boton_generar.grid(row=2, columnspan=4, pady=10)

        self.frame_matrices = ctk.CTkFrame(self.frame)
        self.frame_matrices.grid(row=3, columnspan=4, pady=5)

        self.boton_calcular = ctk.CTkButton(self.frame, text="Calcular", command=self.calcular)
        self.boton_calcular.grid(row=4, columnspan=4, pady=10)

        self.frame.pack(fill=tk.BOTH, expand=True)

    def generar_entradas(self):
        global filas_A, cols_A
        filas_A = int(self.filas_A_entry.get())
        cols_A = int(self.cols_A_entry.get())

        for widget in self.frame_matrices.winfo_children():
            widget.destroy()

        global A_entries
        A_entries = [[ctk.CTkEntry(self.frame_matrices, width=50) for _ in range(cols_A)] for _ in range(filas_A)]

        ctk.CTkLabel(self.frame_matrices, text="Matriz A").grid(row=0, column=0, columnspan=cols_A, pady=5)
        for i in range(filas_A):
            for j in range(cols_A):
                A_entries[i][j].grid(row=i + 1, column=j, padx=5, pady=5)

    def calcular(self):
        A = obtener_matriz(A_entries, filas_A, cols_A)
        if A is None:
            return

        try:
            escalar = float(self.escalar_entry.get())
        except ValueError:
            messagebox.showerror("Error", "El escalar debe ser un número.")
            return

        resultado = multiplicar_matriz_por_escalar(A, escalar)

        self.mostrar_resultado(resultado)

    def mostrar_resultado(self, resultado):
        for widget in self.resultados_frame.winfo_children():
            widget.destroy()

        resultado_frame = ctk.CTkFrame(self.resultados_frame)
        resultado_frame.grid(row=0, column=0, columnspan=4, pady=5)

        # Centrar el título
        ctk.CTkLabel(resultado_frame, text="Resultado de la multiplicación por escalar").grid(row=0, column=0, columnspan=len(resultado[0]), pady=5, sticky="nsew")

        for i in range(len(resultado)):
            for j in range(len(resultado[0])):
                resultado_frame_cell = ctk.CTkFrame(resultado_frame, border_width=1)
                resultado_frame_cell.grid(row=i + 1, column=j, padx=5, pady=5, sticky="nsew")

                resultado_label = ctk.CTkLabel(resultado_frame_cell, text=f"{round(resultado[i][j], 4)}", width=50)
                resultado_label.pack(fill=tk.BOTH, expand=True)

        # Botones para operaciones adicionales en una fila
        self.boton_determinante = ctk.CTkButton(self.resultados_frame, text="Determinante", command=lambda: self.calcular_determinante(resultado))
        self.boton_determinante.grid(row=1, column=0, padx=5)

        self.boton_inversa = ctk.CTkButton(self.resultados_frame, text="Matriz Inversa", command=lambda: self.calcular_inversa(resultado))
        self.boton_inversa.grid(row=1, column=1, padx=5)

        self.boton_transpuesta = ctk.CTkButton(self.resultados_frame, text="Matriz Transpuesta", command=lambda: self.calcular_transpuesta(resultado))
        self.boton_transpuesta.grid(row=1, column=2, padx=5)

        self.boton_rango = ctk.CTkButton(self.resultados_frame, text="Rango", command=lambda: self.calcular_rango(resultado))
        self.boton_rango.grid(row=1, column=3, padx=5)

        self.boton_borrar = ctk.CTkButton(self.resultados_frame, text="Limpiar Entradas", command=self.limpiar_entradas)
        self.boton_borrar.grid(row=2, columnspan=4, pady=10)

    def calcular_determinante(self, resultado):
        if len(resultado) != len(resultado[0]):
            messagebox.showerror("Error", "El determinante solo se puede calcular para matrices cuadradas.")
            return
        
        det = round(np.linalg.det(resultado), 4)
        self.mostrar_resultado_opciones("Determinante:", [[det]])

    def calcular_inversa(self, resultado):
        if len(resultado) != len(resultado[0]):
            messagebox.showerror("Error", "La inversa solo se puede calcular para matrices cuadradas.")
            return
        
        try:
            inversa = np.round(np.linalg.inv(resultado), 4)
            self.mostrar_resultado_opciones("Matriz Inversa:", inversa)
        except np.linalg.LinAlgError:
            messagebox.showerror("Error", "La matriz no tiene inversa.")

    def calcular_transpuesta(self, resultado):
        transpuesta = np.round(np.transpose(resultado), 4)
        self.mostrar_resultado_opciones("Matriz Transpuesta:", transpuesta)

    def calcular_rango(self, resultado):
        rango = round(np.linalg.matrix_rank(resultado), 4)
        self.mostrar_resultado_opciones("Rango de la Matriz:", [[rango]])

    def mostrar_resultado_opciones(self, operacion, resultado):
        for widget in self.resultados_adicionales:
            widget.destroy()

        resultado_op_frame = ctk.CTkFrame(self.resultados_frame)
        resultado_op_frame.grid(row=3, columnspan=4, pady=5)

        self.resultados_adicionales.append(resultado_op_frame)

        ctk.CTkLabel(resultado_op_frame, text=operacion).grid(row=0, column=0, columnspan=len(resultado[0]), pady=5)

        for i in range(len(resultado)):
            for j in range(len(resultado[0])):
                resultado_op_cell = ctk.CTkFrame(resultado_op_frame, border_width=1)
                resultado_op_cell.grid(row=i + 1, column=j, padx=5, pady=5)

                resultado_op_label = ctk.CTkLabel(resultado_op_cell, 
                                  text=f"{round(resultado[i][j], 4)}", 
                                  width=50)
                resultado_op_label.pack(fill=tk.BOTH, expand=True)

    def borrar_resultados(self):
        for widget in self.resultados_frame.winfo_children():
            widget.destroy()

    def limpiar_entradas(self):
        # Limpiar las entradas de tamaño de las matrices
        self.filas_A_entry.delete(0, tk.END)
        self.cols_A_entry.delete(0, tk.END)
        self.escalar_entry.delete(0,tk.END)
        
        # Limpiar las entradas de las matrices generadas
        for widget in self.frame_matrices.winfo_children():
            widget.destroy()

        # Limpiar resultados anteriores
        self.borrar_resultados()

if __name__ == "__main__":
    root = tk.Tk()
    app = Escalar(root)
    root.mainloop()
