import tkinter as tk
from tkinter import ttk
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
        self.frame = tk.Frame(master, bg="#cccccc")
        self.crear_widgets()

    def crear_widgets(self):
        self.montserrat = font.Font(family="Montserrat", size=10)

        # Entradas para el tamaño de las matrices en una sola línea
        self.tamano_A_label = ttk.Label(
            self.frame,
            text="Tamaño de la matriz A (Filas x Columnas):",
            font=self.montserrat,
            background="#cccccc",
        )
        self.tamano_A_label.grid(row=0, column=0, padx=5, pady=5)

        self.filas_A_entry = ttk.Entry(self.frame, width=5, font=self.montserrat)
        self.filas_A_entry.grid(row=0, column=1, padx=(0, 2), pady=5)

        self.x_label = ttk.Label(
            self.frame, text="x", font=self.montserrat, background="#cccccc"
        )
        self.x_label.grid(row=0, column=2, padx=2, pady=5)

        self.cols_A_entry = ttk.Entry(self.frame, width=5, font=self.montserrat)
        self.cols_A_entry.grid(row=0, column=3, padx=(2, 0), pady=5)

        # Entradas para el tamaño de la matriz B
        self.tamano_B_label = ttk.Label(
            self.frame,
            text="Tamaño de la matriz B (Filas x Columnas):",
            font=self.montserrat,
            background="#cccccc",
        )
        self.tamano_B_label.grid(row=1, column=0, padx=5, pady=5)

        self.filas_B_entry = ttk.Entry(self.frame, width=5, font=self.montserrat)
        self.filas_B_entry.grid(row=1, column=1, padx=(0, 2), pady=5)

        self.x_label_B = ttk.Label(
            self.frame, text="x", font=self.montserrat, background="#cccccc"
        )
        self.x_label_B.grid(row=1, column=2, padx=2, pady=5)

        self.cols_B_entry = ttk.Entry(self.frame, width=5, font=self.montserrat)
        self.cols_B_entry.grid(row=1, column=3, padx=(2, 0), pady=5)

        # Botón para generar las entradas
        self.boton_generar = ttk.Button(
            self.frame, text="Generar Entradas", command=self.generar_entradas
        )
        self.boton_generar.grid(row=2, columnspan=4, pady=10)

        # Frame para las matrices de entrada
        self.frame_matrices = tk.Frame(self.frame, bg="#cccccc")
        self.frame_matrices.grid(row=3, columnspan=4, pady=5)

        # Botón para calcular
        self.boton_calcular = ttk.Button(
            self.frame, text="Calcular", command=self.calcular
        )
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
            messagebox.showerror(
                "Error",
                "El número de columnas de A debe ser igual al número de filas de B.",
            )
            return

        # Limpiar entradas anteriores
        for widget in self.frame_matrices.winfo_children():
            widget.destroy()

        global A_entries, B_entries
        A_entries = [
            [
                ttk.Entry(self.frame_matrices, width=5, font=self.montserrat)
                for _ in range(cols_A)
            ]
            for _ in range(filas_A)
        ]
        B_entries = [
            [
                ttk.Entry(self.frame_matrices, width=5, font=self.montserrat)
                for _ in range(cols_B)
            ]
            for _ in range(filas_B)
        ]

        # Etiqueta para la matriz A
        ttk.Label(
            self.frame_matrices,
            text="Matriz A",
            font=self.montserrat,
            background="#cccccc",
        ).grid(row=0, column=0, columnspan=cols_A, pady=5)
        for i in range(filas_A):
            for j in range(cols_A):
                A_entries[i][j].grid(row=i + 1, column=j, padx=5, pady=5)

        # Separador (centrado)
        ttk.Label(
            self.frame_matrices, text="x", font=self.montserrat, background="#cccccc"
        ).grid(row=0, column=cols_A, padx=5, pady=5)

        # Etiqueta para la matriz B
        ttk.Label(
            self.frame_matrices,
            text="Matriz B",
            font=self.montserrat,
            background="#cccccc",
        ).grid(row=0, column=cols_A + 1, columnspan=cols_B, pady=5)
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
            messagebox.showerror(
                "Error",
                "El número de columnas de A debe ser igual al número de filas de B.",
            )
            return

        # Mostrar el resultado
        self.mostrar_resultado(resultado)

    def mostrar_resultado(self, resultado):
        resultado_frame = tk.Frame(self.frame, bg="#cccccc")
        resultado_frame.grid(row=5, columnspan=4, pady=5)

        ttk.Label(
            resultado_frame,
            text="Resultado de la multiplicación",
            font=self.montserrat,
            background="#cccccc",
        ).grid(row=0, column=0, columnspan=len(resultado[0]), pady=5)

        # Crear tabla para mostrar los resultados
        for i in range(len(resultado)):
            for j in range(len(resultado[0])):
                resultado_frame_cell = tk.Frame(
                    resultado_frame, bg="#848a90", bd=1
                )  # Cambia "#39a0fc" por el color de borde deseado
                resultado_frame_cell.grid(row=i + 1, column=j, padx=5, pady=5)

                resultado_label = ttk.Label(
                    resultado_frame_cell,
                    text=f"{resultado[i][j]}",
                    font=self.montserrat,
                    background="#ffffff",  # Cambiar el color de fondo aquí
                    width=5,
                )
                resultado_label.pack(fill=tk.BOTH, expand=True)

        # Añadir un botón para borrar resultados
        self.boton_borrar = ttk.Button(
            resultado_frame, text="Borrar Resultados", command=self.borrar_resultados
        )
        self.boton_borrar.grid(
            row=len(resultado) + 1, columnspan=len(resultado[0]), pady=10
        )

        # Configurar el peso de las columnas
        for j in range(len(resultado[0])):
            resultado_frame.columnconfigure(j, weight=1)

    def borrar_resultados(self):
        # Borrar el marco de resultados
        for widget in self.frame.winfo_children():
            if (
                isinstance(widget, tk.Frame) and widget != self.frame_matrices
            ):  # Asegúrate de no borrar las matrices
                widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calculadora de Multiplicación")
    root.geometry("1000x800")
    root.configure(bg="#cccccc")

    # Crear el estilo de ttk
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure(
        "TButton",
        background="#39a0fc",
        foreground="white",
        font=("Helvetica", 10, "bold"),
    )
    style.map("TButton", background=[("active", "#206098")])

    # Instanciar la clase Matriz
    matriz_app = Matriz(root)

    root.mainloop()
