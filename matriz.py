import tkinter as tk
from tkinter import messagebox
from tkinter import font

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
        self.frame = tk.Frame(master)
        self.crear_widgets()

    def crear_widgets(self):
        self.montserrat = font.Font(family="Montserrat", size=10)

        # Entradas para el tamaño de las matrices en una sola línea
        self.tamano_A_label = tk.Label(self.frame, text="Tamaño de la matriz A (Filas x Columnas):", font=self.montserrat)
        self.tamano_A_label.grid(row=0, column=0, padx=5, pady=5)

        self.filas_A_entry = tk.Entry(self.frame, width=5, font=self.montserrat)
        self.filas_A_entry.grid(row=0, column=1, padx=(0, 2), pady=5)

        self.x_label = tk.Label(self.frame, text="x", font=self.montserrat)
        self.x_label.grid(row=0, column=2, padx=2, pady=5)

        self.cols_A_entry = tk.Entry(self.frame, width=5, font=self.montserrat)
        self.cols_A_entry.grid(row=0, column=3, padx=(2, 0), pady=5)

        # Entradas para el tamaño de la matriz B
        self.tamano_B_label = tk.Label(self.frame, text="Tamaño de la matriz B (Filas x Columnas):", font=self.montserrat)
        self.tamano_B_label.grid(row=1, column=0, padx=5, pady=5)

        self.filas_B_entry = tk.Entry(self.frame, width=5, font=self.montserrat)
        self.filas_B_entry.grid(row=1, column=1, padx=(0, 2), pady=5)

        self.x_label_B = tk.Label(self.frame, text="x", font=self.montserrat)
        self.x_label_B.grid(row=1, column=2, padx=2, pady=5)

        self.cols_B_entry = tk.Entry(self.frame, width=5, font=self.montserrat)
        self.cols_B_entry.grid(row=1, column=3, padx=(2, 0), pady=5)

        # Botón para generar las entradas
        self.boton_generar = tk.Button(self.frame, text="Generar Entradas", command=self.generar_entradas, font=self.montserrat)
        self.boton_generar.grid(row=2, columnspan=4, pady=10)

        # Frame para las matrices de entrada
        self.frame_matrices = tk.Frame(self.frame)
        self.frame_matrices.grid(row=3, columnspan=4, pady=5)

        # Botón para calcular
        self.boton_calcular = tk.Button(self.frame, text="Calcular", command=self.calcular, font=self.montserrat)
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
        A_entries = [[tk.Entry(self.frame_matrices, width=5, font=self.montserrat) for _ in range(cols_A)] for _ in range(filas_A)]
        B_entries = [[tk.Entry(self.frame_matrices, width=5, font=self.montserrat) for _ in range(cols_B)] for _ in range(filas_B)]

        # Etiqueta para la matriz A
        tk.Label(self.frame_matrices, text="Matriz A", font=self.montserrat).grid(row=0, column=0, columnspan=cols_A, pady=5)
        for i in range(filas_A):
            for j in range(cols_A):
                A_entries[i][j].grid(row=i+1, column=j, padx=5, pady=5)

        # Separador (centrado)
        tk.Label(self.frame_matrices, text="x", font=self.montserrat).grid(row=0, column=cols_A, padx=5, pady=5)

        # Etiqueta para la matriz B
        tk.Label(self.frame_matrices, text="Matriz B", font=self.montserrat).grid(row=0, column=cols_A + 1, columnspan=cols_B, pady=5)
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
        resultado_frame = tk.Frame(self.frame)
        resultado_frame.grid(row=5, columnspan=4, pady=5)

        tk.Label(resultado_frame, text="Resultado de la multiplicación", font=self.montserrat).grid(row=0, column=0, columnspan=cols_B, pady=5)
        for i in range(len(resultado)):
            for j in range(len(resultado[0])):
                tk.Label(resultado_frame, text=str(resultado[i][j]), font=self.montserrat).grid(row=i+1, column=j, padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Multiplicación de Matrices")
    app = Matriz(root)
    root.mainloop()
