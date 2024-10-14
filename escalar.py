import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font


class Escalar:
    def __init__(self, master):
        self.frame = tk.Frame(master, bg="#cccccc")
        self.montserrat = font.Font(family="Montserrat", size=10)
        self.crear_widgets()
        self.frame.pack(fill=tk.BOTH, expand=True)

    def crear_widgets(self):
        # Tamaño de la matriz A
        self.tamano_A_label = ttk.Label(self.frame, text="Tamaño de la matriz A (Filas x Columnas):", font=self.montserrat, background="#cccccc")
        self.tamano_A_label.grid(row=0, column=0, padx=5, pady=5)

        self.filas_A_entry = ttk.Entry(self.frame, width=5, font=self.montserrat)
        self.filas_A_entry.grid(row=0, column=1, padx=(0, 2), pady=5)

        self.x_label = ttk.Label(self.frame, text="x", font=self.montserrat, background="#cccccc")
        self.x_label.grid(row=0, column=2, padx=2, pady=5)

        self.cols_A_entry = ttk.Entry(self.frame, width=5, font=self.montserrat)
        self.cols_A_entry.grid(row=0, column=3, padx=(2, 0), pady=5)

        # Escalar
        self.escalar_label = ttk.Label(self.frame, text="Escalar:", font=self.montserrat, background="#cccccc")
        self.escalar_label.grid(row=2, column=0, padx=5, pady=5)

        self.escalar_entry = ttk.Entry(self.frame, width=5, font=self.montserrat)
        self.escalar_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botón para generar entradas
        self.boton_generar = ttk.Button(self.frame, text="Generar Entradas", command=self.generar_entradas)
        self.boton_generar.grid(row=1, columnspan=4, pady=10)

        # Frame para las matrices
        self.frame_matrices = tk.Frame(self.frame, bg="#cccccc")
        self.frame_matrices.grid(row=3, columnspan=4, pady=5)

        # Botón para calcular
        self.boton_calcular = ttk.Button(self.frame, text="Calcular", command=self.calcular)
        self.boton_calcular.grid(row=4, columnspan=4, pady=10)

        # Frame para resultados
        self.resultado_frame = tk.Frame(self.frame, bg="#cccccc")
        self.resultado_frame.grid(row=5, columnspan=4, pady=5)

    def generar_entradas(self):
        try:
            filas = int(self.filas_A_entry.get())
            cols = int(self.cols_A_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa números válidos para las filas y columnas.")
            return

        # Limpiar el frame de matrices
        for widget in self.frame_matrices.winfo_children():
            widget.destroy()

        # Crear entradas para la matriz
        self.matriz_A = []
        for i in range(filas):
            fila = []
            for j in range(cols):
                entry = ttk.Entry(self.frame_matrices, width=5, font=self.montserrat)
                entry.grid(row=i, column=j, padx=5, pady=5)
                fila.append(entry)
            self.matriz_A.append(fila)

    def calcular(self):
        # Obtener los valores de la matriz y el escalar
        try:
            escalar = float(self.escalar_entry.get())
            matriz_A_valores = [[float(self.matriz_A[i][j].get()) for j in range(len(self.matriz_A[i]))] for i in range(len(self.matriz_A))]

            # Multiplicación por escalar
            resultado = [[escalar * valor for valor in fila] for fila in matriz_A_valores]

            # Limpiar el marco de resultados
            for widget in self.resultado_frame.winfo_children():
                widget.destroy()

            # Mostrar resultado en el marco de resultados
            ttk.Label(self.resultado_frame, text="Resultado de la multiplicación", font=self.montserrat, background="#cccccc").grid(row=0, column=0, columnspan=len(resultado[0]), pady=5)
            for i in range(len(resultado)):
                for j in range(len(resultado[0])):
                    resultado_entry = ttk.Entry(self.resultado_frame, width=5, font=self.montserrat)
                    resultado_entry.grid(row=i + 1, column=j, padx=5, pady=5)
                    resultado_entry.insert(0, resultado[i][j])
                    resultado_entry.config(state="readonly")

            # Añadir un botón para borrar resultados
            self.boton_borrar = ttk.Button(self.resultado_frame, text="Borrar Resultados", command=self.borrar_resultados)
            self.boton_borrar.grid(row=len(resultado) + 1, columnspan=len(resultado[0]), pady=10)

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa números válidos.")

    def borrar_resultados(self):
        # Borrar el marco de resultados
        for widget in self.resultado_frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Multiplicación de Matriz por Escalar")
    root.configure(bg="#cccccc")

    # Crear el estilo de ttk
    style = ttk.Style(root)
    style.theme_use('clam')
    style.configure("TButton", background="#39a0fc", foreground="white", font=("Helvetica", 10, "bold"))
    style.map("TButton", background=[('active', '#206098')])

    app = Escalar(root)
    root.mainloop()
