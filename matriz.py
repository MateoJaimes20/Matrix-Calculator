import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
import numpy as np

def multiplicar_matrices(A, B):
    filas_A, cols_A = len(A), len(A[0])
    filas_B, cols_B = len(B), len(B[0])

    if cols_A != filas_B:
        return None

    resultado = [[0] * cols_B for _ in range(filas_A)]

    for i in range(filas_A):
        for j in range(cols_B):
            for k in range(cols_A):
                resultado[i][j] += A[i][k] * B[k][j]
    
    return resultado

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

class Matriz:
    def __init__(self, master):
        self.frame = tk.Frame(master, bg="#cccccc")
        self.crear_widgets()
        self.resultados_frame = tk.Frame(self.frame, bg="#cccccc")  # Frame para resultados
        self.resultados_frame.grid(row=7, columnspan=4, pady=5)  # Posicionar el frame de resultados
        self.resultados_adicionales = []  # Almacenará las etiquetas de resultados adicionales

    def crear_widgets(self):
        self.montserrat = font.Font(family="Montserrat", size=10)

        # Entradas para el tamaño de las matrices en una sola línea
        self.tamano_A_label = ttk.Label(self.frame, text="Tamaño de la matriz A (Filas x Columnas):", font=self.montserrat, background="#cccccc")
        self.tamano_A_label.grid(row=0, column=0, padx=5, pady=5)

        self.filas_A_entry = ttk.Entry(self.frame, width=5, font=self.montserrat)
        self.filas_A_entry.grid(row=0, column=1, padx=(0, 2), pady=5)

        self.x_label = ttk.Label(self.frame, text="x", font=self.montserrat, background="#cccccc")
        self.x_label.grid(row=0, column=2, padx=2, pady=5)

        self.cols_A_entry = ttk.Entry(self.frame, width=5, font=self.montserrat)
        self.cols_A_entry.grid(row=0, column=3, padx=(2, 0), pady=5)

        # Entradas para el tamaño de la matriz B
        self.tamano_B_label = ttk.Label(self.frame, text="Tamaño de la matriz B (Filas x Columnas):", font=self.montserrat, background="#cccccc")
        self.tamano_B_label.grid(row=1, column=0, padx=5, pady=5)

        self.filas_B_entry = ttk.Entry(self.frame, width=5, font=self.montserrat)
        self.filas_B_entry.grid(row=1, column=1, padx=(0, 2), pady=5)

        self.x_label_B = ttk.Label(self.frame, text="x", font=self.montserrat, background="#cccccc")
        self.x_label_B.grid(row=1, column=2, padx=2, pady=5)

        self.cols_B_entry = ttk.Entry(self.frame, width=5, font=self.montserrat)
        self.cols_B_entry.grid(row=1, column=3, padx=(2, 0), pady=5)

        # Botón para generar las entradas
        self.boton_generar = ttk.Button(self.frame, text="Generar Entradas", command=self.generar_entradas)
        self.boton_generar.grid(row=2, columnspan=4, pady=10)

        # Frame para las matrices de entrada
        self.frame_matrices = tk.Frame(self.frame, bg="#cccccc")
        self.frame_matrices.grid(row=3, columnspan=4, pady=5)

        # Botón para calcular
        self.boton_calcular = ttk.Button(self.frame, text="Calcular", command=self.calcular)
        self.boton_calcular.grid(row=4, columnspan=4, pady=10)

        self.frame.pack(fill=tk.BOTH, expand=True)

    def generar_entradas(self):
        global filas_A, cols_A, filas_B, cols_B
        filas_A = int(self.filas_A_entry.get())
        cols_A = int(self.cols_A_entry.get())
        filas_B = int(self.filas_B_entry.get())
        cols_B = int(self.cols_B_entry.get())

        # Validar que el número de columnas de A sea igual al número de filas de B
        if cols_A != filas_B:
            messagebox.showerror("Error", "El número de columnas de A debe ser igual al número de filas de B.")
            return

        # Limpiar entradas anteriores
        for widget in self.frame_matrices.winfo_children():
            widget.destroy()

        global A_entries, B_entries
        A_entries = [[ttk.Entry(self.frame_matrices, width=5, font=self.montserrat) for _ in range(cols_A)] for _ in range(filas_A)]
        B_entries = [[ttk.Entry(self.frame_matrices, width=5, font=self.montserrat) for _ in range(cols_B)] for _ in range(filas_B)]

        # Etiqueta para la matriz A
        ttk.Label(self.frame_matrices, text="Matriz A", font=self.montserrat, background="#cccccc").grid(row=0, column=0, columnspan=cols_A, pady=5)
        for i in range(filas_A):
            for j in range(cols_A):
                A_entries[i][j].grid(row=i + 1, column=j, padx=5, pady=5)

        # Separador (centrado)
        ttk.Label(self.frame_matrices, text="x", font=self.montserrat, background="#cccccc").grid(row=0, column=cols_A, padx=5, pady=5)

        # Etiqueta para la matriz B
        ttk.Label(self.frame_matrices, text="Matriz B", font=self.montserrat, background="#cccccc").grid(row=0, column=cols_A + 1, columnspan=cols_B, pady=5)
        for i in range(filas_B):
            for j in range(cols_B):
                B_entries[i][j].grid(row=i + 1, column=cols_A + 1 + j, padx=5, pady=5)

    def calcular(self):
        A = obtener_matriz(A_entries, filas_A, cols_A)
        B = obtener_matriz(B_entries, filas_B, cols_B)

        if A is None or B is None:
            return

        resultado = multiplicar_matrices(A, B)
        if resultado is None:
            messagebox.showerror("Error", "El número de columnas de A debe ser igual al número de filas de B.")
            return

        # Mostrar el resultado
        self.mostrar_resultado(resultado)

    def mostrar_resultado(self, resultado):
        # Limpiar resultados anteriores
        for widget in self.resultados_frame.winfo_children():
            widget.destroy()

        resultado_frame = tk.Frame(self.resultados_frame, bg="#cccccc")
        resultado_frame.pack(pady=5)

        ttk.Label(resultado_frame, text="Resultado de la multiplicación", font=self.montserrat, background="#cccccc").grid(row=0, column=0, columnspan=len(resultado[0]), pady=5)

        # Crear tabla para mostrar los resultados
        for i in range(len(resultado)):
            for j in range(len(resultado[0])):
                resultado_frame_cell = tk.Frame(resultado_frame, bg="#848a90", bd=1)  # Cambia "#39a0fc" por el color de borde deseado
                resultado_frame_cell.grid(row=i + 1, column=j, padx=5, pady=5)

                resultado_label = ttk.Label(resultado_frame_cell, 
                                             text=f"{resultado[i][j]}", 
                                             font=self.montserrat, 
                                             background="#ffffff",  # Cambiar el color de fondo aquí
                                             width=5)
                resultado_label.pack(fill=tk.BOTH, expand=True)

        # Botones para operaciones adicionales
        self.boton_determinante = ttk.Button(self.resultados_frame, text="Determinante", command=lambda: self.calcular_determinante(resultado))
        self.boton_determinante.pack(side=tk.LEFT, padx=5)

        self.boton_inversa = ttk.Button(self.resultados_frame, text="Matriz Inversa", command=lambda: self.calcular_inversa(resultado))
        self.boton_inversa.pack(side=tk.LEFT, padx=5)

        self.boton_transpuesta = ttk.Button(self.resultados_frame, text="Matriz Transpuesta", command=lambda: self.calcular_transpuesta(resultado))
        self.boton_transpuesta.pack(side=tk.LEFT, padx=5)

        self.boton_rango = ttk.Button(self.resultados_frame, text="Rango", command=lambda: self.calcular_rango(resultado))
        self.boton_rango.pack(side=tk.LEFT, padx=5)

        self.boton_borrar = ttk.Button(self.resultados_frame, text="Borrar Resultados", command=self.borrar_resultados)
        self.boton_borrar.pack(side=tk.LEFT, padx=5)

    def calcular_determinante(self, resultado):
        if len(resultado) != len(resultado[0]):
            messagebox.showerror("Error", "El determinante solo se puede calcular para matrices cuadradas.")
            return
        
        det = np.linalg.det(resultado)
        self.mostrar_resultado_opciones("Determinante:", [[det]])

    def calcular_inversa(self, resultado):
        if len(resultado) != len(resultado[0]):
            messagebox.showerror("Error", "La inversa solo se puede calcular para matrices cuadradas.")
            return
        
        try:
            inversa = np.linalg.inv(resultado)
            self.mostrar_resultado_opciones("Inversa:", inversa)
        except np.linalg.LinAlgError:
            messagebox.showerror("Error", "La matriz no es invertible.")

    def calcular_transpuesta(self, resultado):
        transpuesta = np.transpose(resultado)
        self.mostrar_resultado_opciones("Transpuesta:", transpuesta)

    def calcular_rango(self, resultado):
        rango = np.linalg.matrix_rank(resultado)
        self.mostrar_resultado_opciones("Rango:", [[rango]])

    def mostrar_resultado_opciones(self, operacion, resultado):
        # Limpiar resultados anteriores de opciones adicionales
        for widget in self.resultados_frame.winfo_children():
            widget.destroy()

        resultado_frame = tk.Frame(self.resultados_frame, bg="#cccccc")
        resultado_frame.pack(pady=5)

        ttk.Label(resultado_frame, text=f"{operacion}", font=self.montserrat, background="#cccccc").grid(row=0, column=0, columnspan=len(resultado[0]), pady=5)

        for i in range(len(resultado)):
            for j in range(len(resultado[0])):
                resultado_frame_cell = tk.Frame(resultado_frame, bg="#848a90", bd=1)
                resultado_frame_cell.grid(row=i + 1, column=j, padx=5, pady=5)

                resultado_label = ttk.Label(resultado_frame_cell, 
                                            text=f"{resultado[i][j]:.2f}", 
                                            font=self.montserrat, 
                                            background="#ffffff",  
                                            width=5)
                resultado_label.pack(fill=tk.BOTH, expand=True)

            # Botón para volver a la multiplicación
        boton_volver = ttk.Button(
            resultado_frame, 
            text="Volver a Multiplicación", 
            command=self.calcular
        )
        boton_volver.grid(row=len(resultado) + 1, columnspan=len(resultado[0]), pady=10)

    def borrar_resultados(self):
        for widget in self.resultados_frame.winfo_children():
            widget.destroy()
        self.resultados_adicionales.clear()  # Limpiar la lista de resultados adicionales



if __name__ == "__main__":
    root = tk.Tk()
    app = Matriz(root)
    root.mainloop()
