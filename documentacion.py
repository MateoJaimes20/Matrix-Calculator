import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Documentacion:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        
        # Crear un Message widget
        self.message = tk.Message(self.frame, text=self.get_documentacion_text(), justify=tk.LEFT, bg="#f0f0f0", padx=10)
        self.message.pack(fill=tk.BOTH, expand=True)

        # Permitir que el frame principal se expanda
        self.frame.pack(fill=tk.BOTH, expand=True)

    def get_documentacion_text(self):
        return (
            "Documentación para la Calculadora de Multiplicación de Matrices y Escalares.\n\n"
            "Este programa permite realizar operaciones de multiplicación de matrices y escalares de manera sencilla y rápida.\n\n"
            "### Instrucciones Generales:\n\n"
            "1. **Seleccionar Modo**: \n"
            "   Al inicio, elige entre \"Multiplicación de Matrices\" o \"Multiplicación por Escalar\" según la operación que desees realizar.\n\n"
            "2. **Entrada de Datos**:\n"
            "   - **Multiplicación de Matrices**:\n"
            "     - Debes ingresar las dimensiones de las matrices que deseas multiplicar...\n\n"
            "   - **Multiplicación por Escalar**:\n"
            "     - Ingresa el valor del escalar (un número real) que deseas multiplicar...\n\n"
            "3. **Calcular**: \n"
            "   Después de ingresar todos los datos, haz clic en el botón \"Calcular\" para ver el resultado...\n\n"
            "### Funcionalidades Adicionales:\n\n"
            " - **Determinante**: Puedes calcular el determinante de una matriz cuadrada...\n\n"
            " - **Inversa**: Esta función te permite obtener la matriz inversa...\n\n"
            " - **Transpuesta**: La transposición de una matriz consiste en intercambiar sus filas por columnas...\n\n"
            " - **Rango**: El rango de una matriz indica el número máximo de columnas linealmente independientes...\n\n"
            "### Consejos Importantes:\n\n"
            " - **Validación de Datos**: Asegúrate de que los datos ingresados sean correctos...\n\n"
            " - **Errores Comunes**: Verifica siempre las dimensiones antes de proceder...\n\n"
            "### Ejemplo de Uso:\n"
            " - Para multiplicar dos matrices, selecciona \"Multiplicación de Matrices\"...\n\n"
            "Disfruta usando la calculadora y aprovecha al máximo sus funciones!"
        )
