import customtkinter as ctk

class Documentacion:
    def __init__(self, parent):
        # Crear frame con scrollbar
        self.frame = ctk.CTkScrollableFrame(parent, width=630, height=680)
        self.frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

        # Crear título principal
        self.titulo = ctk.CTkLabel(self.frame, text="Manual de Usuario: Calculadora de Matrices", font=("Helvetica", 24, "bold"), padx=10, pady=10)
        self.titulo.pack(fill=ctk.BOTH, pady=10)

        # Sección de introducción
        self.introduccion_frame = self.crear_seccion(self.frame, "Introducción")
        self.crear_texto_instrucciones(
            self.introduccion_frame, 
            "Este programa te permite realizar operaciones con matrices y escalares de manera rápida y eficiente. "
            "Soporta operaciones básicas como multiplicación por escalar, multiplicación de matrices, así como "
            "funciones adicionales como cálculo del determinante, matriz inversa, transpuesta y rango. Los resultados "
            "se redondean automáticamente a 4 decimales para mayor claridad."
        )

        # Instrucciones Generales
        self.instrucciones_frame = self.crear_seccion(self.frame, "Instrucciones Generales")
        instrucciones_text = (
            "1. **Seleccionar Modo**: Elige entre \"Multiplicación de Matrices\" o \"Multiplicación por Escalar\".\n\n"
            "2. **Entrada de Datos**:\n"
            "   - **Multiplicación de Matrices**: Ingresa las dimensiones de las dos matrices y llena cada una de ellas.\n"
            "   - **Multiplicación por Escalar**: Ingresa las dimensiones de la matriz y luego el valor del escalar.\n\n"
            "3. **Calcular**: Haz clic en \"Calcular\" para obtener el resultado de la operación. Recuerda que los resultados "
            "se redondearán automáticamente a 4 decimales.\n"
        )
        self.crear_texto_instrucciones(self.instrucciones_frame, instrucciones_text)

        # Modo 1: Multiplicación de Matrices
        self.modo_matrices_frame = self.crear_seccion(self.frame, "Modo 1: Multiplicación de Matrices")
        modo_matrices_text = (
            "1. Ingresa las dimensiones de las matrices (filas x columnas).\n"
            "2. Llena las matrices con los valores que desees (se pueden ingresar números enteros o decimales).\n"
            "3. Presiona el botón \"Calcular\" para ver el resultado de la multiplicación de las matrices.\n\n"
            "**Nota**: Asegúrate de que el número de columnas de la primera matriz coincida con el número de filas de la segunda matriz.\n"
        )
        self.crear_texto_instrucciones(self.modo_matrices_frame, modo_matrices_text)

        # Modo 2: Multiplicación por Escalar
        self.modo_escalar_frame = self.crear_seccion(self.frame, "Modo 2: Multiplicación por Escalar")
        modo_escalar_text = (
            "1. Ingresa las dimensiones de la matriz.\n"
            "2. Llena la matriz con los valores que desees (puedes ingresar enteros o decimales).\n"
            "3. Ingresa el valor del escalar que deseas usar para multiplicar la matriz.\n"
            "4. Presiona \"Calcular\" para obtener el resultado de la multiplicación.\n\n"
            "**Nota**: Los resultados estarán redondeados a 4 decimales.\n"
        )
        self.crear_texto_instrucciones(self.modo_escalar_frame, modo_escalar_text)

        # Funcionalidades adicionales
        self.funcionalidades_frame = self.crear_seccion(self.frame, "Funcionalidades Adicionales")
        funcionalidades_text = (
            "- **Determinante**: Calcula el determinante de una matriz cuadrada. Solo está disponible para matrices cuadradas.\n\n"
            "- **Inversa**: Obtén la matriz inversa si existe. Solo se puede calcular para matrices cuadradas que tengan inversa.\n\n"
            "- **Transpuesta**: Intercambia las filas por columnas de una matriz, obteniendo su transpuesta.\n\n"
            "- **Rango**: Calcula el rango de la matriz, es decir, el número de filas o columnas linealmente independientes.\n"
        )
        self.crear_texto_instrucciones(self.funcionalidades_frame, funcionalidades_text)

        # Consejos importantes
        self.consejos_frame = self.crear_seccion(self.frame, "Consejos Importantes")
        consejos_text = (
            "- **Validación de Datos**: Asegúrate de que todos los datos sean correctos antes de realizar los cálculos.\n"
            "- **Errores Comunes**: Verifica que las dimensiones de las matrices sean compatibles para realizar las operaciones. "
            "Si las matrices no tienen el tamaño adecuado, recibirás un error.\n\n"
            "- **Decimales**: Puedes ingresar números decimales para todas las entradas. El resultado siempre se redondeará a 4 decimales."
        )
        self.crear_texto_instrucciones(self.consejos_frame, consejos_text)

        # Ejemplo de uso
        self.ejemplo_frame = self.crear_seccion(self.frame, "Ejemplo de Uso")
        ejemplo_text = (
            "Para multiplicar dos matrices, selecciona \"Multiplicación de Matrices\", ingresa las dimensiones de ambas matrices, "
            "llena los valores de las matrices, y presiona \"Calcular\". El resultado se mostrará redondeado a 4 decimales.\n\n"
            "Si seleccionas \"Multiplicación por Escalar\", ingresa las dimensiones de la matriz, los valores de la matriz, y el valor del escalar. "
            "Presiona \"Calcular\" para obtener el resultado."
        )
        self.crear_texto_instrucciones(self.ejemplo_frame, ejemplo_text)

    def crear_seccion(self, parent, titulo):
        """Crea una sección con un título destacado."""
        seccion_frame = ctk.CTkFrame(parent, corner_radius=10)
        seccion_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

        seccion_titulo = ctk.CTkLabel(
            seccion_frame, text=titulo, font=("Helvetica", 18, "bold"), padx=10, pady=5
        )
        seccion_titulo.pack(anchor="w", pady=5)

        return seccion_frame

    def crear_texto_instrucciones(self, parent, texto):
        """Crea un texto con estilo para instrucciones o descripciones."""
        instrucciones_label = ctk.CTkLabel(
            parent, text=texto, font=("Helvetica", 13), justify="left", wraplength=500, padx=10
        )
        instrucciones_label.pack(fill=ctk.BOTH, pady=5)

# Crear ventana para probar la clase Documentacion
if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("650x700")
    root.title("Documentación")
    app = Documentacion(root)
    root.mainloop()
